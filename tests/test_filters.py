import unittest
from json_journal.filters import filter_balances_to_expenses


class TestBalanceToExpenses(unittest.TestCase):

    def test_simplecase(self):
        # Given
        journal = {
            'expense:eatingout': 100, 'assets:current': -150,
            'expense:groceries': 50
        }

        expected_expenses = {
            'expense:eatingout': 100,
            'expense:groceries': 50,
        }

        # When
        actual_expenses = filter_balances_to_expenses(journal)

        # Then
        self.assertEqual(expected_expenses, actual_expenses)
