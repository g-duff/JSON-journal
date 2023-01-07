from matplotlib import pyplot as plt
import json


def load_balance(json_file):
    with open(json_file, 'r') as file:
        balances = json.load(file)
    return balances


def create_pie_chart(balances):
    account_list = []
    amount_list = []
    for account, amount in balances.items():
        account_list.append(account)
        amount_list.append(abs(amount))
    plt.pie(amount_list, labels = account_list)


if __name__ == '__main__':
    json_file = 'balance.json'
    balances_data = load_balance(json_file)
    #create_pie_chart(balances_data)

    expenses_json = 'expenses.json'
    expenses_data = load_balance(expenses_json)
    create_pie_chart(expenses_data)
    plt.show()

