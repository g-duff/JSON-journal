import unittest
from read_data import separate_expenses
from read_data import total_profit

class TestSeparateExpenses(unittest.TestCase):

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
        actual_expenses = separate_expenses(journal)

        # Then
        self.assertEqual(expected_expenses, actual_expenses)


class TestTotalBalance(unittest.TestCase):

    def test_simplecase(self):
        # Given
        journal = [
            {
                'income:job': -1000, 'assets:current' : 1000, 
                'expenses:groceries' : 50, 'assets:current' : -50
            }
        ]
        expected_total = 950  #(income * (-1)) - expenses) 

        # When
        actual_total = total_profit(journal)

        # Then
        self.assertEqual(expected_total, actual_total)