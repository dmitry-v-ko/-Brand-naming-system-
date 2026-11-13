import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / 'checks/session/validate_session.py'


def block(kind, value):
    return f'```{kind}\n{json.dumps(value, ensure_ascii=False)}\n```\n'


def state():
    return {
        'session_id': 'synthetic', 'received_through': 'T08',
        'brand_brief': 'Personal scheduling assistant; UK, English; no medical claims.',
        'conversation_language': 'ru', 'customer_language': 'en',
        'language_basis': 'T02', 'category_descriptor': 'Scheduling assistant',
        'current_stage': 'EXPORT', 'active_branch': None,
        'latest_user_decision': {'turn': 'T08', 'quote': 'Выбираю Luma. Завершаем.'},
        'favorites': [{'id': 'B1-C1', 'name': 'Luma'}],
        'name_checks': {'B1-C1': {'check_id': 'NC2', 'status': 'clarify'}},
        'next_options': ['stop'],
    }


def shortlist(data):
    return (block('session-state', data) + '\n## Active favorites\n\n'
            '| Candidate ID | Exact name | Notes |\n|---|---|---|\n'
            '| B1-C1 | Luma | Selected in T08 |\n\n'
            '## History\n\n| B0-C1 | Olda | Removed in T04 |\n')


def plan():
    return {
        'pass_id': 'P1', 'anchors': [{
            'parent_id': 'B0-C1', 'defect': 'Close-category market use',
            'method': 'phonetic-invention', 'source_recognition': 'optional',
            'recognition_basis': 'T05: a different sound is welcome',
            'slots': ['B1-C1', 'B1-C2', 'B1-C3'],
        }], 'sound_controls': ['B1-C2', 'B1-C3'],
    }


def result(data, ids):
    # Independent encoding of the documented plan fingerprint format.
    digest = hashlib.sha256(json.dumps(data, sort_keys=True,
        ensure_ascii=False, separators=(',', ':')).encode()).hexdigest()
    return {'plan_sha256': digest, 'generated_ids': ids}


class SessionChecks(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.exists(), 'Session validation gate is missing on main')
        spec = importlib.util.spec_from_file_location('session_checks', SCRIPT)
        self.gate = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.gate)

    def test_current_state_and_archived_favorite_are_distinct(self):
        data = state()
        self.gate.validate_state(block('session-state', data), shortlist(data), 'T08')

    def test_new_question_does_not_change_origin_of_latest_selection(self):
        data = state()
        data['received_through'] = 'T09'
        self.gate.validate_state(block('session-state', data), shortlist(data), 'T09')

    def test_empty_shortlist_is_valid(self):
        data = state()
        data['favorites'] = []
        saved = shortlist(data).replace('| B1-C1 | Luma | Selected in T08 |', '')
        self.gate.validate_state(block('session-state', data), saved, 'T08')

    def test_reordering_favorites_is_detected(self):
        data = state()
        data['favorites'].append({'id': 'B1-C2', 'name': 'Nera'})
        saved = shortlist(data).replace('| B1-C1 | Luma | Selected in T08 |',
            '| B1-C2 | Nera | Selected |\n| B1-C1 | Luma | Selected in T08 |')
        with self.assertRaisesRegex(ValueError, 'order'):
            self.gate.validate_state(block('session-state', data), saved, 'T08')

    def test_stale_header_cannot_be_fixed_by_appending_a_later_event(self):
        old = state()
        old.update(received_through='T03', favorites=[{'id': 'B0-C1', 'name': 'Olda'}])
        log = block('session-state', old) + '\nT08: Luma selected; Olda removed.\n'
        with self.assertRaisesRegex(ValueError, 'received_through'):
            self.gate.validate_state(log, shortlist(state()), 'T08')

    def test_matching_stale_headers_still_fail_against_received_turn(self):
        data = state()
        data['received_through'] = 'T03'
        with self.assertRaisesRegex(ValueError, 'received_through'):
            self.gate.validate_state(block('session-state', data), shortlist(data), 'T08')

    def test_check_status_and_latest_decision_must_agree(self):
        for field, value in [('name_checks', {}), ('latest_user_decision', {'turn': 'T02', 'quote': 'Wait'})]:
            with self.subTest(field=field):
                other = state()
                other[field] = value
                with self.assertRaisesRegex(ValueError, 'differ|decision'):
                    self.gate.validate_state(block('session-state', state()), shortlist(other), 'T08')

    def test_favorite_rows_must_match_order_and_exact_spelling(self):
        data = state()
        for bad in [shortlist(data).replace('| B1-C1 | Luma |', '| B1-C1 | Lumo |'),
                    shortlist(data).replace('| B1-C1 | Luma | Selected in T08 |', ''),
                    shortlist(data).replace('| B1-C1 | Luma |', '| B0-C1 | Olda |')]:
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, 'favorites'):
                self.gate.validate_state(block('session-state', data), bad, 'T08')

    def test_missing_or_duplicate_current_block_is_not_silently_migrated(self):
        for bad in ['- received_through: T08', block('session-state', state()) * 2]:
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, 'one session-state'):
                self.gate.validate_state(bad, shortlist(state()), 'T08')

    def test_refinement_plan_and_empty_no_yield_result_are_valid(self):
        data = plan()
        self.gate.validate_refinement(data)
        self.gate.validate_refinement(data, result(data, []))
        self.gate.validate_refinement(data, result(data, ['B1-C1', 'B1-C2', 'B1-C3']))

    def test_four_sound_variants_cannot_override_three_slot_anchor_limit(self):
        data = plan()
        data['anchors'][0]['slots'].append('B1-C4')
        with self.assertRaisesRegex(ValueError, 'three'):
            self.gate.validate_refinement(data)

    def test_rejected_fourth_candidate_still_counts(self):
        data = plan()
        with self.assertRaisesRegex(ValueError, 'unplanned'):
            self.gate.validate_refinement(data, result(data, ['B1-C1', 'B1-C2', 'B1-C3', 'B1-C4']))

    def test_parent_must_exist_in_plan_before_generation(self):
        data = plan()
        del data['anchors'][0]['parent_id']
        with self.assertRaisesRegex(ValueError, 'parent_id'):
            self.gate.validate_refinement(data)

    def test_controls_share_slots_and_one_two_control_budget(self):
        for controls in [['outside'], ['B1-C1', 'B1-C2', 'B1-C3']]:
            data = plan()
            data['sound_controls'] = controls
            with self.subTest(controls=controls), self.assertRaisesRegex(ValueError, 'controls'):
                self.gate.validate_refinement(data)

    def test_plan_cannot_be_reassigned_after_results(self):
        data = plan()
        output = result(data, ['B1-C1'])
        data['anchors'][0]['parent_id'] = 'B0-C2'
        with self.assertRaisesRegex(ValueError, 'fingerprint'):
            self.gate.validate_refinement(data, output)

    def test_duplicate_slots_and_third_anchor_fail(self):
        for mutate in ['duplicate', 'third']:
            data = plan()
            if mutate == 'duplicate':
                data['anchors'][0]['slots'][2] = 'B1-C1'
            else:
                data['anchors'] *= 3
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                self.gate.validate_refinement(data)

    def test_russian_report_allows_english_names_and_customer_examples(self):
        report = block('report-language', {'narrative': 'ru', 'customer_examples': 'en'})
        report += '# Luma\n\nПроверка неполная. Нужно уточнить похожие обозначения перед запуском.\n'
        report += block('customer-example', {'text': 'I use Luma to plan my day.'})
        report += '\n> The quoted source is in English.\n'
        self.gate.validate_report(report, 'ru', 'en')

    def test_russian_report_from_template_keeps_stable_english_keys(self):
        template = (SCRIPT.parents[2] / 'templates/NAME_CHECK.md').read_text()
        fields = template.split('## Findings and next actions')[0]
        labels = [line.split(':', 1)[0] for line in fields.splitlines() if line.startswith('- ')]
        report = block('report-language', {'narrative': 'ru', 'customer_examples': 'en'})
        report += '# Предварительная проверка\n\n'
        report += '\n'.join(label + ': неизвестно' for label in labels)
        report += '\n\nПроверка неполная. Требуется уточнить похожие обозначения. '
        report += 'До запуска необходимо проверить реестры и оценить оставшиеся риски.'
        self.gate.validate_report(report, 'ru', 'en')

    def test_english_report_in_russian_session_is_rejected_even_if_mislabeled(self):
        for label in ['en', 'ru']:
            report = block('report-language', {'narrative': label, 'customer_examples': 'en'})
            report += '# Luma\n\nThe check is incomplete. Further investigation is needed before launch.\n'
            with self.subTest(label=label), self.assertRaisesRegex(ValueError, 'language|Cyrillic'):
                self.gate.validate_report(report, 'ru', 'en')

    def test_customer_language_is_not_inferred_from_conversation(self):
        report = block('report-language', {'narrative': 'ru', 'customer_examples': 'ru'})
        report += 'Проверка неполная. Нужна дополнительная проверка названия.'
        with self.assertRaisesRegex(ValueError, 'customer'):
            self.gate.validate_report(report, 'ru', 'en')

    def test_cli_fails_closed_without_writing_inputs(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'plan.json'
            bad = plan()
            bad['anchors'][0]['slots'].append('B1-C4')
            raw = json.dumps(bad)
            path.write_text(raw)
            run = subprocess.run([sys.executable, '-B', str(SCRIPT), 'refinement', str(path)],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 1, run.stderr)
            self.assertFalse(json.loads(run.stdout)['ok'])
            self.assertEqual(path.read_text(), raw)
            path.write_text('{broken')
            run = subprocess.run([sys.executable, '-B', str(SCRIPT), 'refinement', str(path)],
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 2)

    def test_cli_runs_documented_state_report_and_refinement_flow(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            data = state()
            (path / 'EXPLORATION_LOG.md').write_text(block('session-state', data))
            (path / 'SHORTLIST.md').write_text(shortlist(data))
            report = block('report-language', {'narrative': 'ru', 'customer_examples': 'en'})
            report += 'Проверка неполная. Требуется уточнить похожие обозначения перед запуском.'
            (path / 'report.md').write_text(report)
            (path / 'plan.json').write_text(json.dumps(plan()))
            def run(*args):
                return subprocess.run([sys.executable, '-B', str(SCRIPT), *map(str, args)],
                                      capture_output=True, text=True)
            for args in [('state', path, 'T08'), ('report', path / 'report.md', 'ru', 'en')]:
                checked = run(*args)
                self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
            preflight = run('refinement', path / 'plan.json')
            self.assertEqual(preflight.returncode, 0, preflight.stdout)
            output = {'plan_sha256': json.loads(preflight.stdout)['plan_sha256'],
                      'generated_ids': ['B1-C1']}
            result_path = path / 'result.json'
            result_path.write_text(json.dumps(output))
            checked = run('refinement', path / 'plan.json', result_path)
            self.assertEqual(checked.returncode, 0, checked.stdout)
            result_path.write_text('null')
            checked = run('refinement', path / 'plan.json', result_path)
            self.assertEqual(checked.returncode, 1, checked.stdout)


if __name__ == '__main__':
    unittest.main()
