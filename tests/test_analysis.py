# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
import unittest
from json_journal import data_analysis


class test_total_profit_happy_path(unittest.TestCase):

    def test_simplecase(self):
        # Given
        balances = {
            'income:job': -1000, 'assets:current': 950,
            'expense:groceries': 50
        }

        expected_income = -1000
        expected_expenses = 50
        expected_profit = (expected_income * (-1)) - expected_expenses

        # When
        actual_profit = data_analysis.total_profit(balances)

        # Then
        self.assertEqual(expected_profit, actual_profit)


class test_cumulative_profit_happy_path(unittest.TestCase):

    def test_simplecase(self):
        # Given
        ledger = [
            {
                "date" : "2022-11-01",
                "description": "pay day",
                "entries": [
                    {"account": "income:job", "amount": -2000},
                    {"account": "assets:tsb", "amount": 2000}
                ]
            },

            {
                "date" : "2022-11-01",
                "description": "food",
                "entries": [
                    {"account": "expense:food", "amount": 20},
                    {"account": "assets:tsb", "amount": -20}
                ]
            },

            {
                "date" : "2022-11-03",
                "description": "gym membership",
                "entries": [
                    {"account": "expense:gym", "amount": 20},
                    {"account": "assets:tsb", "amount": -20}
                ]
            }]

        expected_dates = ['2022-11-01', '2022-11-03']
        expected_cumulative_profits = [1980, 1960]

        # When
        actual_dates, actual_cumulative_profit = data_analysis.cumulative_profit(
            ledger)

        # Then
        self.assertEqual(expected_dates, actual_dates)
        self.assertEqual(expected_cumulative_profits, actual_cumulative_profit)
