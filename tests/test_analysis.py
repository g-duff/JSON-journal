import unittest
from json_journal.main import total_profit

class TestTotalProfit(unittest.TestCase):

    def test_simplecase(self):
        # Given
        journal = [
            {
                'income:job': -1000, 'assets:current' : 1000, 
                'expenses:groceries' : 50, 'assets:current' : -50
            }
        ]

        expected_income = 1000
        expected_expenses = -50
        expected_profit = (-1 * expected_income)  - expected_expenses

        # When
        actual_profit = total_profit(journal)

        # Then
        self.assertEqual(expected_profit, actual_profit)