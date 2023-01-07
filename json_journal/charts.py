from matplotlib import pyplot as plt
import json


def load_balance(json_file):
    with open(json_file, 'r') as file:
        balances = json.load(file)
    return balances


def create_pie_chart(balances, axes):
    account_names = []
    account_balances = []
    for account_name, account_balance in balances.items():
        account_names.append(account_name)
        account_balances.append(abs(account_balance))
    axes.pie(account_balances, labels = account_names)


if __name__ == '__main__':
    balance_json_file = 'balance.json'
    balances_data = load_balance(balance_json_file)

    expenses_json_file = 'expenses.json'
    expenses_data = load_balance(expenses_json_file)

    fig, (left_axes, right_axes) = plt.subplots(ncols=2)
    create_pie_chart(balances_data, left_axes)
    create_pie_chart(expenses_data, right_axes)
    plt.show()
