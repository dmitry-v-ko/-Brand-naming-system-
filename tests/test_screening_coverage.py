import importlib.util
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    'coverage', Path(__file__).parents[1] / 'checks/name-screening/validate_coverage.py')
coverage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(coverage)


def ledger():
    return {
        'check_id': 'fixture-01', 'scope_revision': '1',
        'planned_query_ids': ['Q1'], 'scope_gaps': [], 'findings': [],
        'queries': [{
            'id': 'Q1', 'office': 'UKIPO', 'mode': 'Exact', 'query': 'aster',
            'source_url': 'https://trademarks.ipo.gov.uk/ipo-tmtext',
            'checked_at': '2026-11-11',
            'filters': {'territories': ['UK'], 'classes': 'all', 'statuses': 'all'},
            'state': 'complete', 'settled': True, 'filters_verified': True,
            'displayed_count': 0, 'pages_expected': 1,
            'pages': [{'page': 1, 'record_ids': []}], 'gap': ''
        }]
    }


class CoverageTests(unittest.TestCase):
    def test_settled_zero_is_complete(self):
        self.assertTrue(coverage.validate(ledger())['coverage_complete'])

    def test_loading_zero_cannot_pass(self):
        data = ledger()
        data['queries'][0]['settled'] = False
        self.assertFalse(coverage.validate(data)['coverage_complete'])

    def test_missing_planned_query_cannot_disappear(self):
        data = ledger()
        data['planned_query_ids'].append('Q2')
        self.assertFalse(coverage.validate(data)['coverage_complete'])

    def test_partial_pages_fail_and_series_duplicates_are_counted(self):
        data = ledger()
        query = data['queries'][0]
        query.update(displayed_count=3, pages_expected=2,
                     pages=[{'page': 1, 'record_ids': ['UKIPO:UK1', 'UKIPO:UK1']}])
        self.assertFalse(coverage.validate(data)['coverage_complete'])
        query['pages'].append({'page': 2, 'record_ids': ['UKIPO:UK2']})
        result = coverage.validate(data)
        self.assertTrue(result['coverage_complete'])
        self.assertEqual(result['queries'][0]['unique_records'], 2)
        self.assertEqual(result['queries'][0]['duplicate_rows'], 1)

    def test_repeated_page_does_not_fill_missing_page(self):
        data = ledger()
        data['queries'][0].update(displayed_count=2, pages_expected=2,
            pages=[{'page': 1, 'record_ids': ['EM:1']}, {'page': 1, 'record_ids': ['EM:2']}])
        self.assertFalse(coverage.validate(data)['coverage_complete'])

    def test_unverified_filters_and_blocked_record_fail(self):
        data = ledger()
        data['queries'][0]['filters_verified'] = False
        self.assertFalse(coverage.validate(data)['coverage_complete'])
        data = ledger()
        data['findings'] = [{'record_id': 'XX1', 'material': True,
            'primary_verified': False, 'source_url': 'https://example.org/record',
            'next_action': 'Open the issuing office record by number.'}]
        result = coverage.validate(data)
        self.assertFalse(result['coverage_complete'])
        self.assertTrue(result['potential_conflict'])

    def test_material_finding_requires_next_action(self):
        data = ledger()
        data['findings'] = [{'record_id': 'XX1', 'material': True,
            'primary_verified': True, 'source_url': 'https://example.org/record',
            'next_action': ''}]
        self.assertFalse(coverage.validate(data)['coverage_complete'])

    def test_conflict_and_completeness_are_independent(self):
        data = ledger()
        data['findings'] = [{'record_id': 'XX1', 'material': True,
            'primary_verified': True, 'source_url': 'https://example.org/record',
            'next_action': 'Compare the actual goods with a specialist.'}]
        result = coverage.validate(data)
        self.assertTrue(result['coverage_complete'])
        self.assertTrue(result['potential_conflict'])
        data['scope_gaps'] = ['Pronunciation not checked']
        self.assertFalse(coverage.validate(data)['coverage_complete'])

    def test_empty_plan_and_malformed_data_fail_closed(self):
        for data in ({}, {'planned_query_ids': []}, None, ledger()):
            if isinstance(data, dict) and data.get('check_id'):
                data['queries'][0]['displayed_count'] = True
            with self.subTest(data=data):
                self.assertFalse(coverage.validate(data)['coverage_complete'])

    def test_complete_query_cannot_hide_a_gap(self):
        data = ledger()
        data['queries'][0]['gap'] = 'Missing page detail'
        self.assertFalse(coverage.validate(data)['coverage_complete'])

    def test_names_are_not_record_identifiers(self):
        data = ledger()
        data['queries'][0].update(displayed_count=2,
            pages=[{'page': 1, 'record_ids': ['aster', 'aster']}])
        self.assertFalse(coverage.validate(data)['coverage_complete'])

    def test_zero_results_need_one_observed_page(self):
        data = ledger()
        data['queries'][0].update(pages_expected=2,
            pages=[{'page': 1, 'record_ids': []}, {'page': 2, 'record_ids': []}])
        self.assertFalse(coverage.validate(data)['coverage_complete'])


if __name__ == '__main__':
    unittest.main()
