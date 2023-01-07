from matplotlib import pyplot as plt
from json_journal import file_io

def create_pie_chart(balances, axes):
    account_names = []
    account_balances = []
    for account_name, account_balance in balances.items():
        account_names.append(account_name)
        account_balances.append(abs(account_balance))
    axes.pie(account_balances, labels = account_names)


if __name__ == '__main__':
    balance_json_file = 'balance.json'
    balances_data = file_io.load_json_file(balance_json_file)

    expenses_json_file = 'expenses.json'
    expenses_data = file_io.load_json_file(expenses_json_file)

    fig, (left_axes, right_axes) = plt.subplots(ncols=2)
    create_pie_chart(balances_data, left_axes)
    create_pie_chart(expenses_data, right_axes)
    plt.show()
