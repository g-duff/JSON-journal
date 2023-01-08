def calculate_balance(ledger):
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


def total_profit(all_balances):
    expenses = 0
    income = 0
    for account in all_balances:
        if account.startswith("expense:"):
            expenses += all_balances[account]
        else:
            pass
    for account in all_balances:
        if account.startswith("income:"):
            income += all_balances[account]
        else:
            pass
    total = (income * (-1)) - expenses
    return total
