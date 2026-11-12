#!/usr/bin/env python3
"""Read-only gates for session persistence, bounded generation and report language."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import unicodedata


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def ids(value):
    return (isinstance(value, list) and all(text(item) for item in value)
            and len(value) == len(set(value)))


def block(document, kind):
    matches = re.findall(r'^```' + re.escape(kind) + r'\s*\n(.*?)^```\s*$',
                         document, re.M | re.S)
    require(len(matches) == 1, f'Expected exactly one {kind} block')
    value = json.loads(matches[0])
    require(isinstance(value, dict), f'{kind} must be an object')
    return value


def validate_state(log, shortlist, received_through):
    current = block(log, 'session-state')
    saved = block(shortlist, 'session-state')
    require(text(received_through), 'Supply the latest actually received turn')
    for data in (current, saved):
        require(data.get('received_through') == received_through,
                'received_through differs from the actual received turn')
        for field in ('session_id', 'brand_brief', 'conversation_language',
                      'language_basis', 'category_descriptor', 'current_stage'):
            require(text(data.get(field)), f'Missing current {field}')
        for field in ('customer_language', 'active_branch'):
            require(field in data and (data[field] is None or text(data[field])),
                    f'Missing or invalid {field}; use null for unknown')
        decision = data.get('latest_user_decision')
        require(isinstance(decision, dict) and text(decision.get('turn'))
                and text(decision.get('quote')), 'Latest decision must cite its received turn and quote')
        require(isinstance(data.get('name_checks'), dict), 'Missing current name_checks')
        require(isinstance(data.get('next_options'), list), 'Missing next_options')
        favorites = data.get('favorites')
        require(isinstance(favorites, list) and all(
            isinstance(row, dict) and text(row.get('id')) and text(row.get('name'))
            for row in favorites), 'Invalid favorites')
        require(ids([row['id'] for row in favorites]), 'Duplicate favorites')
    require(current == saved, 'Current session-state blocks differ')
    sections = re.findall(r'^## Active favorites\s*\n(.*?)(?=^## |\Z)', shortlist, re.M | re.S)
    require(len(sections) == 1, 'Expected one Active favorites section')
    rows = []
    for line in sections[0].splitlines():
        if not line.startswith('|'):
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if cells[0] == 'Candidate ID' or re.fullmatch(r'[:\- ]+', cells[0]):
            continue
        require(len(cells) >= 2, 'Invalid favorites table row')
        rows.append({'id': cells[0], 'name': cells[1]})
    require(rows == current['favorites'], 'Active favorites rows differ in IDs, order or spelling')


def fingerprint(plan):
    payload = json.dumps(plan, sort_keys=True, ensure_ascii=False, separators=(',', ':'))
    return hashlib.sha256(payload.encode()).hexdigest()


def validate_refinement(plan, result=None):
    require(isinstance(plan, dict) and text(plan.get('pass_id')), 'Missing pass_id')
    anchors = plan.get('anchors')
    require(isinstance(anchors, list) and 1 <= len(anchors) <= 2, 'Use one or two initial anchors')
    slots, parents = [], []
    for anchor in anchors:
        require(isinstance(anchor, dict), 'Invalid anchor')
        for field in ('parent_id', 'defect', 'method', 'recognition_basis'):
            require(text(anchor.get(field)), f'Missing anchor {field} before generation')
        require(anchor.get('source_recognition') in ('required', 'optional'),
                'Freeze source_recognition before generation')
        allocated = anchor.get('slots')
        require(ids(allocated) and 1 <= len(allocated) <= 3,
                'Each anchor has at most three unique slots, including sound replacements')
        slots.extend(allocated)
        parents.append(anchor['parent_id'])
    require(ids(parents) and ids(slots), 'Duplicate parents or slots')
    controls = plan.get('sound_controls')
    require(ids(controls) and len(controls) <= 2 and set(controls) <= set(slots),
            'Sound controls: at most two per pass, reserved inside anchor slots')
    if result is not None:
        require(isinstance(result, dict) and result.get('plan_sha256') == fingerprint(plan),
                'Plan fingerprint changed after preflight')
        generated = result.get('generated_ids')
        require(ids(generated), 'List every generated ID once, including rejected forms')
        require(set(generated) <= set(slots), 'Generated unplanned variants; rejected forms count too')


def validate_report(document, conversation_language, customer_language):
    declared = block(document, 'report-language')
    require(declared.get('narrative') == conversation_language, 'Report narrative language mismatch')
    require(declared.get('customer_examples') == customer_language, 'Report customer language mismatch')
    require(text(conversation_language), 'Missing conversation language')
    narrative = re.sub(r'^```[^\n]*\n.*?^```\s*$', '', document, flags=re.M | re.S)
    narrative = '\n'.join(line for line in narrative.splitlines()
                          if not line.lstrip().startswith(('>', '|', '<!--')))
    narrative = re.sub(r'^\s*- [a-z][a-z0-9_]*(?:\s*/\s*[a-z][a-z0-9_]*)*:\s*',
                       '', narrative, flags=re.M)
    narrative = re.sub(r'https?://\S+', '', narrative)
    letters = [char for char in narrative if char.isalpha()]
    require(len(letters) >= 20, 'Report needs narrative prose outside examples, quotes and tables')
    # shortcut: script sanity for ru/en only; semantic language review is still required.
    script = {'ru': 'CYRILLIC', 'en': 'LATIN'}.get(conversation_language.lower().split('-')[0])
    if script:
        matching = sum(script in unicodedata.name(char, '') for char in letters)
        require(matching / len(letters) > .5,
                f'Report narrative must predominantly use {script.title()} script; review language')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest='mode', required=True)
    state = modes.add_parser('state')
    state.add_argument('session_directory', type=Path)
    state.add_argument('received_through')
    refinement = modes.add_parser('refinement')
    refinement.add_argument('plan', type=Path)
    refinement.add_argument('result', type=Path, nargs='?')
    report = modes.add_parser('report')
    report.add_argument('document', type=Path)
    report.add_argument('conversation_language')
    report.add_argument('customer_language')
    args = parser.parse_args()
    output = {'ok': False, 'issues': []}
    try:
        if args.mode == 'state':
            validate_state((args.session_directory / 'EXPLORATION_LOG.md').read_text(encoding='utf-8'),
                           (args.session_directory / 'SHORTLIST.md').read_text(encoding='utf-8'),
                           args.received_through)
        elif args.mode == 'refinement':
            plan = json.loads(args.plan.read_text(encoding='utf-8'))
            result = json.loads(args.result.read_text(encoding='utf-8')) if args.result else None
            require(not args.result or isinstance(result, dict), 'Result must be an object')
            validate_refinement(plan, result)
            output['plan_sha256'] = fingerprint(plan)
        else:
            validate_report(args.document.read_text(encoding='utf-8'),
                            args.conversation_language, args.customer_language)
            output['manual_check'] = 'Review actual narrative and customer-example languages; not language detection'
        output['ok'] = True
        code = 0
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        output['issues'].append(str(error))
        code = 2
    except ValueError as error:
        output['issues'].append(str(error))
        code = 1
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
