# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
import unittest
from json_journal import preconditioning


class TestSortLedger(unittest.TestCase):

    def test_ledgersorted_happypath(self):
        # Given
        ledger = [
            {
                "date": "2022-11-01",
                "description": "bills",
                "entries": [
                    {"account": "expense:bills", "amount": 650},
                    {"account": "assets:bank", "amount": -650}
                ]
            },

            {
                "date": "2022-12-03",
                "description": "gym membership",
                "entries": [
                    {"account": "expense:gym", "amount": 10},
                    {"account": "assets:bank", "amount": -10}
                ]
            },

            {
                "date": "2022-11-10",
                "description": "savings",
                "entries": [
                    {"account": "assets:savings", "amount": 50},
                    {"account": "assets:bank", "amount": -50}
                ]
            }
        ]

        expected_ledger = [
            {
                "date": "2022-11-01",
                "description": "bills",
                "entries": [
                    {"account": "expense:bills", "amount": 650},
                    {"account": "assets:bank", "amount": -650}
                ]
            },

            {
                "date": "2022-11-10",
                "description": "savings",
                "entries": [
                    {"account": "assets:savings", "amount": 50},
                    {"account": "assets:bank", "amount": -50}
                ]
            },

            {
                "date": "2022-12-03",
                "description": "gym membership",
                "entries": [
                    {"account": "expense:gym", "amount": 10},
                    {"account": "assets:bank", "amount": -10}
                ]
            }
        ]

        # When
        actual_ledger = preconditioning.sort_journal_by_date(ledger)

        # Then
        self.assertEqual(expected_ledger, actual_ledger)

    def test_ledgersortnodates_error(self):
        # Given
        ledger = [
            {
                "description": "bills",
                "entries": [
                    {"account": "expense:bills", "amount": 650},
                    {"account": "assets:bank", "amount": -650}
                ]
            },

            {
                "description": "gym membership",
                "entries": [
                    {"account": "expense:gym", "amount": 10},
                    {"account": "assets:bank", "amount": -10}
                ]
            },

            {
                "description": "savings",
                "entries": [
                    {"account": "assets:savings", "amount": 50},
                    {"account": "assets:bank", "amount": -50}
                ]
            }
        ]

        # When / Then
        with self.assertRaises(KeyError):
            preconditioning.sort_journal_by_date(ledger)


class TestEntriesSumToZero(unittest.TestCase):

    def test_doessumtozero_happypath(self):
        # Given
        ledger = [
            {
                "date": "2022-11-01",
                "description": "bills",
                "entries": [
                    {"account": "expense:bills", "amount": 650},
                    {"account": "assets:bank", "amount": -650}
                ]
            },

            {
                "date": "2022-12-03",
                "description": "gym membership",
                "entries": [
                    {"account": "expense:gym", "amount": 10},
                    {"account": "assets:bank", "amount": -10}
                ]
            },

            {
                "date": "2022-11-10",
                "description": "savings",
                "entries": [
                    {"account": "assets:savings", "amount": 50},
                    {"account": "assets:bank", "amount": -50}
                ]
            }
        ]

        expected_amount_sum = 0

        # When
        actual_amount_sum = preconditioning.check_entries_sum_to_zero(ledger)

        # Then
        self.assertEqual(expected_amount_sum, actual_amount_sum)


    def test_doesnotsumtozero_warningappears(self):
        # Given
        ledger = [
            {
                "date": "2022-11-01",
                "description": "bills",
                "entries": [
                    {"account": "expense:bills", "amount": 650},
                    {"account": "assets:bank", "amount": -650}
                ]
            },

            {
                "date": "2022-12-03",
                "description": "gym membership",
                "entries": [
                    {"account": "expense:gym", "amount": 10},
                    {"account": "assets:bank", "amount": -1}
                ]
            },

            {
                "date": "2022-11-10",
                "description": "savings",
                "entries": [
                    {"account": "assets:savings", "amount": 50},
                    {"account": "assets:bank", "amount": -50}
                ]
            }
        ]

        # When/Then
        with self.assertRaises(Warning):
            preconditioning.check_entries_sum_to_zero(ledger)
