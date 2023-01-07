def separate_out_entities(ledger, all_entries):
    for transaction in range(len(ledger)):
        entries = (ledger[transaction]['entries'])

        for entry in range(len(entries)):
            amount = (entries[entry])['amount']
            account = (entries[entry])['account']

            if account in all_entries:
                new_amount = amount + all_entries.get(account)
                all_entries[account] = new_amount
            else:
                all_entries[account] = amount


def separate_expenses(all_balances):
    expenses = [[account, all_balances[account]] for account in all_balances if account.startswith("expense:")]
    expenses_dict = dict(expenses)
    return expenses_dict


def separate_main_accounts(all_balances):
    new_balances = {}
    for account in all_balances.keys():
        account_separated = account.split(':')
        for i in range(len(account_separated)):
            main_account = ':'.join(account_separated[:i+1])
            if main_account in new_balances:
                new_balances[main_account] += all_balances[account]
            else:
                new_balances[main_account] = all_balances[account]
    return new_balances