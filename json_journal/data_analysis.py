'''Functions for various analysis on data'''
COLON = ':'

def calculate_balance(ledger):
    '''
    Calculate balance for all entries.

    Parameters
    ----------
    Ledger : dict
        Loaded json file.

    Returns
    -------
    All_balances : dict
        Contains full account names and balances for each account.
    '''
    all_balances = {}
    for transaction in ledger:
        entries = transaction['entries']

        for entry in entries:
            amount = entry['amount']
            account = entry['account']

            if account in all_balances:
                new_amount = amount + all_balances.get(account)
                all_balances[account] = new_amount
            else:
                all_balances[account] = amount
    return all_balances


def parent_account_balances(full_account_name_balances):
    '''
    Calculate balances for all parent accounts.

    Parameters
    ----------
    Full_account_name_balances : dict
        Contains the full account name and corresponding balance.

    Returns
    -------
    New_balances : dict
        Contains balances for each parent account.
    '''
    new_balances = {}
    for full_account_name in full_account_name_balances.keys():
        account_separated = full_account_name.split(COLON)
        for child_account_name in range(len(account_separated)):
            parent_account = COLON.join(account_separated[:child_account_name+1])
            if parent_account in new_balances:
                new_balances[parent_account] += full_account_name_balances[full_account_name]
            else:
                new_balances[parent_account] = full_account_name_balances[full_account_name]
    return new_balances


def total_profit(full_account_name_balances):
    '''
    Calculate the total profit.

    Parameters
    ----------
    Full_account_name_balances : dict
        Contains the full account name and corresponding balance.

    Returns
    -------
    Total : int
        Total profit value.
    '''
    expenses = 0
    income = 0
    for account in full_account_name_balances:
        if account.startswith("expense:"):
            expenses += full_account_name_balances[account]
        if account.startswith("income:"):
            income += full_account_name_balances[account]
        else:
            pass
    total = (income * (-1)) - expenses
    return total
