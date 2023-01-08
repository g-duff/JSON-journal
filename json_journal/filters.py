'''Filter balances to expenses'''

def filter_balances_to_expenses(all_balances):
    '''all_balances -> dictionary with full account name and corresponding balance.
    Returns dictionary of balances where the account name starts with expense'''
    expenses = {account: all_balances[account]
                for account in all_balances if account.startswith("expense:")}
    return expenses
