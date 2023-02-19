# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
import unittest
from json_journal import data_analysis


class TestTotalProfit(unittest.TestCase):

    def test_happypath(self):
        # Given
        balances = {
            'income:job': -1000, 'assets:current': 950,
            'expense:groceries': 50
        }

        expected_income = -1000
        expected_expenses = 50
        expected_profit = - expected_income - expected_expenses

        # When
        actual_profit = data_analysis.total_profit(balances)

        # Then
        self.assertEqual(expected_profit, actual_profit)

    def test_noincome_correctprofit(self):
        # Given
        balances = {
            'assets:current': 950,
            'expense:groceries': 50
        }

        expected_income = 0
        expected_expenses = 50
        expected_profit = - expected_income - expected_expenses

        # When
        actual_profit = data_analysis.total_profit(balances)

        # Then
        self.assertEqual(expected_profit, actual_profit)

    def test_noexpense_correctprofit(self):
        # Given
        balances = {
            'income:job': -1000, 'assets:current': 950
        }

        expected_income = -1000
        expected_expenses = 0
        expected_profit = - expected_income - expected_expenses

        # When
        actual_profit = data_analysis.total_profit(balances)

        # Then
        self.assertEqual(expected_profit, actual_profit)

    def test_noincomeorexpense_correctprofit(self):
        # Given
        balances = {
            'assets:job': -1000, 'assets:current': 950
            }

        expected_income = 0
        expected_expenses = 0
        expected_profit = - expected_income - expected_expenses

        # When
        actual_profit = data_analysis.total_profit(balances)

        # Then
        self.assertEqual(expected_profit, actual_profit)

    def test_emptydictionary(self):
        # Given
        balances = {
            }

        expected_income = 0
        expected_expenses = 0
        expected_profit = - expected_income - expected_expenses

        # When
        actual_profit = data_analysis.total_profit(balances)

        # Then
        self.assertEqual(expected_profit, actual_profit)



class TestCumulativeProfit(unittest.TestCase):

    def test_happypath(self):
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

    def test_missingdateinledger_error(self):
        # Given
        ledger = [
            {
                "description": "pay day",
                "entries": [
                    {"account": "income:job", "amount": -2000},
                    {"account": "assets:tsb", "amount": 2000}
                ]
            },

            {
                "desciption" : "eating out",
                "entries": [
                    {"account": "expense:food", "amount": 20},
                    {"account": "assets:tsb", "amount": -20}
                ]
            },

            {
                "description": "gym membership",
                "entries": [
                    {"account": "expense:gym", "amount": 20},
                    {"account": "assets:tsb", "amount": -20}
                ]
            }]

        # When/Then
        with self.assertRaises(KeyError):
            data_analysis.cumulative_profit(ledger)

    def test_missingdescriptioninledger_noerror(self):
        # Given
        ledger = [
            {
                "date" : "2022-11-01",
                "entries": [
                    {"account": "income:job", "amount": -2000},
                    {"account": "assets:tsb", "amount": 2000}
                ]
            },

            {
                "date" : "2022-11-01",
                "entries": [
                    {"account": "expense:food", "amount": 20},
                    {"account": "assets:tsb", "amount": -20}
                ]
            },

            {
                "date" : "2022-11-03",
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

    def test_emptyentriesinledger_noerror(self):
        # Given
        ledger = [
            {
                "date" : "2022-11-01",
                "description" : "pay day",
                "entries": [
                ]
            },

            {
                "date" : "2022-11-01",
                "description" : "eating out",
                "entries": [
                ]
            },

            {
                "date" : "2022-11-03",
                "description" : "gym membership",
                "entries": [
                ]
            }]

        expected_dates = ['2022-11-01', '2022-11-03']
        expected_cumulative_profits = [0, 0]

        # When
        actual_dates, actual_cumulative_profit = data_analysis.cumulative_profit(
            ledger)

        # Then
        self.assertEqual(expected_dates, actual_dates)
        self.assertEqual(expected_cumulative_profits, actual_cumulative_profit)

    def test_missingentriesinledger_error(self):
        # Given
        ledger = [
            {
                "date" : "2022-11-01",
                "description" : "pay day",
            },

            {
                "date" : "2022-11-01",
                "description" : "eating out",
            },

            {
                "date" : "2022-11-03",
                "description" : "gym membership",
            }]


        # When/Then
        with self.assertRaises(KeyError):
            data_analysis.cumulative_profit(ledger)


class TestCalculateBalance(unittest.TestCase):

    def test_calculatebalance_happypath(self):
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
                "desciption" : "eating out",
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

        expected_balance_dictionary = {
                "income:job" : -2000,
                "assets:tsb" : 1960,
                "expense:food" : 20,
                "expense:gym" : 20
                }

        # When
        actual_balance_dictionary = data_analysis.calculate_balance(ledger)

        # Then
        self.assertEqual(expected_balance_dictionary, actual_balance_dictionary)

    def test_calculatebalance_emptyentries(self):
        # Given
        ledger = [
               {
                "date" : "2022-11-01",
                "description": "pay day",
                "entries": [
                ]
            },

            {
                "date" : "2022-11-01",
                "desciption" : "eating out",
                "entries": [
                ]
            },

            {
                "date" : "2022-11-03",
                "description": "gym membership",
                "entries": [
                ]
            }]

        expected_balance_dictionary = {
                }

        # When
        actual_balance_dictionary = data_analysis.calculate_balance(ledger)

        # Then
        self.assertEqual(expected_balance_dictionary, actual_balance_dictionary)

    def test_calculatebalance_noentrieserror(self):
        # Given
        ledger = [
               {
                "date" : "2022-11-01",
                "description": "pay day",
            },

            {
                "date" : "2022-11-01",
                "desciption" : "eating out",
            },

            {
                "date" : "2022-11-03",
                "description": "gym membership",
            }]

        # When/Then
        with self.assertRaises(KeyError):
            data_analysis.calculate_balance(ledger)


class TestParentAccountBalanceCalculation(unittest.TestCase):

    def test_calculateparentbalance_happypath(self):
        # Given
        full_account_name_balances = {
                "income:job" : -2000,
                "assets:tsb" : 1960,
                "expense:food" : 20,
                "expense:gym" : 20
                }

        expected_parent_balances = {
                "income" : -2000,
                "income:job" : -2000,
                "assets" : 1960,
                "assets:tsb" : 1960,
                "expense" : 40,
                "expense:food" : 20,
                "expense:gym" : 20
                }

        # When
        actual_parent_balances = data_analysis.parent_account_balances(full_account_name_balances)

        # Then
        self.assertEqual(expected_parent_balances, actual_parent_balances)

    def test_calculateparentbalance_emptyinput(self):
        # Given
        full_account_name_balances = {
                }

        expected_parent_balances = {
                }

        # When
        actual_parent_balances = data_analysis.parent_account_balances(full_account_name_balances)

        # Then
        self.assertEqual(expected_parent_balances, actual_parent_balances)
