# pylint: disable = missing-module-docstring, missing-class-docstring, missing-function-docstring
import argparse
import json

from tabulate import tabulate

from json_journal.report import balance


def builder(subparsers: argparse.Action) -> None:
    subparser: argparse.ArgumentParser = subparsers.add_parser(
        'balance')
    subparser.add_argument('--filepath', nargs='?', required=True)
    subparser.set_defaults(handler=handler)


def handler(args):
    filepath = args.filepath

    with open(filepath) as ledgerfile:
        journal = json.load(ledgerfile)

    balances = balance.balance(journal)
    display_output(balances)


def display_output(balances):
    sorted_account_names = sorted(balances.keys())

    output_headers = ['account', 'amount']
    output_rows = ([account_name, balances[account_name]]
                   for account_name in sorted_account_names)

    output_table = tabulate(headers=output_headers, tabular_data=output_rows)
    print(output_table)
