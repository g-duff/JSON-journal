# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring
from tabulate import tabulate


def tabulate_sorted_entries(all_entries, sorted_accounts):
    output_rows = [[account_name, all_entries[account_name]]
                   for account_name in sorted_accounts]
    output_headers = ["Account", "Amount"]
    print(tabulate(output_rows, headers=output_headers))
