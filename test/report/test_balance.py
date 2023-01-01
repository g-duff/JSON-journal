# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
import unittest
from json_journal.report import balance


class TestBalance(unittest.TestCase):

    def test_simplecase(self):
        # Given
        journal = [
            {
                'entries': [
                    {'account': 'assets:current', 'amount': 100},
                    {'account': 'assets:saving', 'amount': -100},
                ],
            },
            {
                'entries': [
                    {'account': 'assets:current', 'amount': -50},
                    {'account': 'expenses:groceries', 'amount': 50},
                ],
            }
        ]
        expected_balance = {
            'assets': -50,
            'assets:current': 50,
            'assets:saving': -100,
            'expenses': 50,
            'expenses:groceries': 50,
        }

        # When
        actual_balance = balance.balance(journal)

        # Then
        self.assertEqual(expected_balance, actual_balance)
