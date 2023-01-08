'''Tabulate data'''
from tabulate import tabulate


def tabulate_sorted_entries(all_entries, sorted_accounts):
    '''all_entries -> dictionary with the full account name and corresponding balance,
    sorted_accounts -> parent account names sorted alphabetically.
    Returns a tabulated table printed in the console'''
    output_rows = [[account_name, all_entries[account_name]]
                   for account_name in sorted_accounts]
    output_headers = ["Account", "Amount"]
    print(tabulate(output_rows, headers=output_headers))
