# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
import unittest
from json_journal.data_analysis import total_profit


class TestTotalProfit(unittest.TestCase):

    def test_simplecase_happypath(self):
        # Given
        balances = {
            'income:job': -1000, 'assets:current': 950,
            'expense:groceries': 50
        }

        expected_income = -1000
        expected_expenses = 50
        expected_profit = (expected_income * (-1)) - expected_expenses

        # When
        actual_profit = total_profit(balances)

        # Then
        self.assertEqual(expected_profit, actual_profit)
