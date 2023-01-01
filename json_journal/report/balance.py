# pylint: disable = missing-module-docstring, missing-function-docstring

def balance(journal):
    balances = individual_account_balances(journal)
    balances = calculate_summaries(balances)
    return balances


def individual_account_balances(ledger):
    balances = {}
    for transaction in ledger:
        for entry in transaction['entries']:
            account_name = entry['account']
            if account_name in balances:
                balances[account_name] += entry['amount']
            else:
                balances[account_name] = entry['amount']
    return balances


def calculate_summaries(balances):
    new_balances = {}
    for account_name in balances.keys():
        account_name_components = account_name.split(':')
        for i in range(len(account_name_components)):
            super_account_name = ':'.join(account_name_components[:i+1])
            if super_account_name in new_balances:
                new_balances[super_account_name] += balances[account_name]
            else:
                new_balances[super_account_name] = balances[account_name]
    return new_balances
