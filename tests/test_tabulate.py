# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
import unittest
from tabulate import tabulate
from json_journal import tabulate_data

class TestTabulateSortedEntries(unittest.TestCase):

    def test_tablulatedata_happypath(self):
        # Given
        all_entries = {
                "income:job" : -2000,
                "assets:tsb" : 1960,
                "expense:eatingout" : 20,
                "expense:gym" : 20
                }

        sorted_accounts = ["assets:tsb", "expense:eatingout", "expense:gym", "income:job"]

        expected_rows = [
                ["assets:tsb", 1960],
                ["expense:eatingout", 20],
                ["expense:gym", 20],
                ["income:job", -2000]
                ]

        expected_result = tabulate(expected_rows, headers=["Account", "Amount"])

        # When
        actual_result = tabulate_data.tabulate_sorted_entries(all_entries, sorted_accounts)

        # Then
        self.assertEqual(expected_result, actual_result)

    def test_tabulatedata_nodata(self):
        # Given
        all_entries = {
                }

        sorted_accounts = []

        expected_rows = [
                ]

        expected_result = tabulate(expected_rows, headers=["Account", "Amount"])

        # When
        actual_result = tabulate_data.tabulate_sorted_entries(all_entries, sorted_accounts)

        # Then
        self.assertEqual(expected_result, actual_result)

    def test_tabulatedata_error(self):
        # Given
        all_entries = {
                }

        sorted_accounts = ["assets:tsb", "expense:eatingout", "expense:gym", "income:job"]

        # When / Then
        with self.assertRaises(KeyError):
            tabulate_data.tabulate_sorted_entries(all_entries, sorted_accounts)
