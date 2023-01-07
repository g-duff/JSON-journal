from tabulate import tabulate
import json


def load_ledger(json_file):
    with open(json_file, 'r') as file:
        ledger = json.load(file)
    return ledger


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


def tabulate_sorted_entries(all_entries, sorted_accounts):
        output_rows = [[i, all_entries[i]] for i in sorted_accounts]
        output_headers = ["Account", "Amount"]
        print(tabulate(output_rows, headers=output_headers))


def save_all_balances_as_json(all_balances):
    balances_json = json.dumps(all_balances, indent = 4) 
    with open("balance.json", 'w+') as file:
        file.write(balances_json)


def save_expenses_as_json(all_expenses):
    expenses_json = json.dumps(all_expenses, indent = 4) 
    with open("expenses.json", 'w+') as file:
        file.write(expenses_json)


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


def total_balance(all_balances):
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


if __name__ == '__main__':

    json_file = 'finances.json'
    entries = {}
    ledger = load_ledger(json_file)

    separate_out_entities(ledger, entries)
    expenses = separate_expenses(entries)
    save_expenses_as_json(expenses)

    save_all_balances_as_json(entries)
    balances = separate_main_accounts(entries)
    sorted_accounts = sorted(balances.keys())
    tabulate_sorted_entries(balances, sorted_accounts)
    print("Total =", total_balance(entries))
