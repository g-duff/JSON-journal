# pylint: disable = import-error, missing-class-docstring, missing-function-docstring, missing-module-docstring

def filter_balances_to_expenses(all_balances):
    expenses = {account: all_balances[account]
                for account in all_balances if account.startswith("expense:")}
    return expenses
