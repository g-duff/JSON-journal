'''Functions for various analysis on data'''

def calculate_balance(ledger):
    '''ledger -> loaded json file.
    Returns dictionary of full account names and balances for each account'''
    all_entries = {}
    for transaction in ledger:
        entries = transaction['entries']

        for entry in entries:
            amount = entry['amount']
            account = entry['account']

            if account in all_entries:
                new_amount = amount + all_entries.get(account)
                all_entries[account] = new_amount
            else:
                all_entries[account] = amount
    return all_entries


def parent_account_balances(full_account_name_balances):
    '''full_account_name_balances -> dictionary of full account names and balances for each account.
    Returns dictionary of parent account and corresponding balances'''
    new_balances = {}
    for full_account_name in full_account_name_balances.keys():
        account_separated = full_account_name.split(':')
        for child_account_name in range(len(account_separated)):
            parent_account = ':'.join(account_separated[:child_account_name+1])
            if parent_account in new_balances:
                new_balances[parent_account] += full_account_name_balances[full_account_name]
            else:
                new_balances[parent_account] = full_account_name_balances[full_account_name]
    return new_balances


def total_profit(full_account_name_balances):
    '''all_balances -> dictionary of full account names and balances for each account.
    Returns profit value'''
    expenses = 0
    income = 0
    for account in full_account_name_balances:
        if account.startswith("expense:"):
            expenses += full_account_name_balances[account]
        else:
            pass
    for account in full_account_name_balances:
        if account.startswith("income:"):
            income += full_account_name_balances[account]
        else:
            pass
    total = (income * (-1)) - expenses
    return total
