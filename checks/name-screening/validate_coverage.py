#!/usr/bin/env python3
"""Check a session ledger, not registry truth or legal availability. No network/writes."""
import json
import re
import sys
from datetime import date
from urllib.parse import urlsplit


def validate(data):
    issues, summaries = [], []
    result = {'coverage_complete': False, 'potential_conflict': False,
              'issues': issues, 'queries': summaries}

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    def text(value):
        return isinstance(value, str) and bool(value.strip())

    def strings(value):
        return isinstance(value, list) and all(text(x) for x in value)

    def integer(value):
        return type(value) is int and value >= 0

    def url(value):
        return text(value) and urlsplit(value).scheme in ('http', 'https') and bool(urlsplit(value).netloc)

    try:
        require(isinstance(data, dict), 'Ledger must be an object')
        for field in ('check_id', 'scope_revision'):
            require(text(data.get(field)), f'Missing {field}')
        plan = data.get('planned_query_ids')
        require(strings(plan) and len(plan) > 0 and len(set(plan)) == len(plan),
                'Plan must contain unique nonempty query IDs')
        require(strings(data.get('scope_gaps')), 'scope_gaps must be a list of strings')
        issues.extend(data['scope_gaps'])
        require(isinstance(data.get('queries'), list), 'queries must be a list')
        seen = set()
        for query in data['queries']:
            require(isinstance(query, dict), 'Query must be an object')
            qid = query.get('id')
            require(text(qid) and qid not in seen, 'Query IDs must be unique and nonempty')
            seen.add(qid)
            require(qid in plan, f'{qid}: query is not in the declared plan')
            for field in ('office', 'mode', 'query', 'checked_at'):
                require(text(query.get(field)), f'{qid}: missing {field}')
            date.fromisoformat(query['checked_at'])
            require(url(query.get('source_url')), f'{qid}: missing source URL')
            filters = query.get('filters')
            require(isinstance(filters, dict), f'{qid}: missing filters')
            for field in ('territories', 'classes', 'statuses'):
                value = filters.get(field)
                require(text(value) or (strings(value) and len(value) > 0), f'{qid}: missing filter {field}')
            require(query.get('state') in ('pending', 'partial', 'blocked', 'complete'), f'{qid}: invalid state')
            if query['state'] != 'complete':
                require(text(query.get('gap')), f'{qid}: unfinished query needs a gap/next query')
                issues.append(f'{qid}: {query["state"]}: {query["gap"]}')
                continue
            require(query.get('gap') == '', f'{qid}: complete query must have an empty gap')
            for field in ('settled', 'filters_verified'):
                if query.get(field) is not True:
                    issues.append(f'{qid}: {field} is not confirmed')
            total, expected = query.get('displayed_count'), query.get('pages_expected')
            require(integer(total) and integer(expected) and expected > 0, f'{qid}: invalid counts')
            require(total != 0 or expected == 1, f'{qid}: zero results require one observed page')
            pages = query.get('pages')
            require(isinstance(pages, list), f'{qid}: missing pages')
            numbers, ids = [], []
            for page in pages:
                require(isinstance(page, dict) and integer(page.get('page')) and page['page'] > 0,
                        f'{qid}: invalid page number')
                require(strings(page.get('record_ids')), f'{qid}: page needs office-qualified record IDs')
                require(all(re.fullmatch(r'[A-Z][A-Z0-9_-]*:[^:]*\d[^:]*', item)
                            for item in page['record_ids']), f'{qid}: use office:number IDs, not mark names')
                numbers.append(page['page'])
                ids.extend(page['record_ids'])
            if sorted(numbers) != list(range(1, expected + 1)):
                issues.append(f'{qid}: missing or repeated pages')
            if len(ids) != total:
                issues.append(f'{qid}: inspected {len(ids)} of {total} displayed rows')
            summaries.append({'id': qid, 'rows': len(ids), 'unique_records': len(set(ids)),
                              'duplicate_rows': len(ids) - len(set(ids))})
        issues.extend(f'{qid}: planned query not performed' for qid in plan if qid not in seen)
        require(isinstance(data.get('findings'), list), 'findings must be a list')
        for finding in data['findings']:
            require(isinstance(finding, dict) and text(finding.get('record_id')), 'Finding needs record_id')
            require(type(finding.get('material')) is bool, 'Finding needs material boolean')
            if finding['material']:
                result['potential_conflict'] = True
                record = finding['record_id']
                if finding.get('primary_verified') is not True or not url(finding.get('source_url')):
                    issues.append(f'{record}: significant record not confirmed in primary source')
                if not text(finding.get('next_action')):
                    issues.append(f'{record}: missing next action')
        result['coverage_complete'] = not issues
    except (ValueError, TypeError, KeyError) as error:
        issues.append(f'Invalid ledger: {error}')
    return result


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 validate_coverage.py /path/to/SCREENING_LEDGER.json', file=sys.stderr)
        return 2
    try:
        with open(sys.argv[1], encoding='utf-8') as handle:
            result = validate(json.load(handle))
    except (OSError, ValueError) as error:
        print(f'Cannot read ledger: {error}', file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['coverage_complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
