# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
import unittest
from json_journal.filters import filter_balances_to_expenses


class TestBalanceToExpenses(unittest.TestCase):

    def test_simplecase_happypath(self):
        # Given
        balances = {
            'expense:eatingout': 100, 'assets:current': -150,
            'expense:groceries': 50
        }

        expected_expenses = {
            'expense:eatingout': 100,
            'expense:groceries': 50,
        }

        # When
        actual_expenses = filter_balances_to_expenses(balances)

        # Then
        self.assertEqual(expected_expenses, actual_expenses)
