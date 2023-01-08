'''Tabulate data'''
from tabulate import tabulate


def tabulate_sorted_entries(all_entries, sorted_accounts):
    '''
     Show balances in a table sorted alphabetically by account name.

    Parameters
    ----------
    All_entries : dict
        Contains the full account name and corresponding balance.
    Sorted_accounts : list
        Contains the parent account names sorted alphabetically.

    Returns
    -------
    Table of balances sorted alphabetically by account name.
    '''
    output_rows = [[account_name, all_entries[account_name]]
                   for account_name in sorted_accounts]
    output_headers = ["Account", "Amount"]
    return tabulate(output_rows, headers=output_headers)
