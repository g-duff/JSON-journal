import json

def load_json_file(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data


def save_all_balances_as_json(all_balances):
    balances_json = json.dumps(all_balances, indent = 4) 
    with open("balance.json", 'w+') as file:
        file.write(balances_json)


def save_expenses_as_json(all_expenses):
    expenses_json = json.dumps(all_expenses, indent = 4) 
    with open("expenses.json", 'w+') as file:
        file.write(expenses_json)