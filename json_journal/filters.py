'''Filter existing data'''


def filter_balances_to_expenses(all_balances):
    '''
    Filter balances to only show expenses.

    Parameters
    ----------
    All_balances : dict
        Contains the full account name and corresponding balance.

    Returns
    -------
    Expenses : dict
        Contains balances where the account name starts with expense
    '''
    expenses = {account: all_balances[account]
                for account in all_balances if account.startswith("expense:")}
    return expenses
