import unittest
from json_journal.filters import filter_balances_to_expenses

class TestBalanceToExpenses(unittest.TestCase):

    def test_simplecase(self):
        # Given
        journal = [
            {
                'expenses:eatingout': 100, 'assets:current' : -100, 
                'expenses:groceries' : 50, 'assets:current' : -50
            },
        ]
        expected_expenses = {
            'expenses:eatingout': 100,
            'expenses:groceries': 50,
        }

        # When
        actual_expenses = filter_balances_to_expenses(journal)

        # Then
        self.assertEqual(expected_expenses, actual_expenses)
