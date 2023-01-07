def create_pie_chart(balances, axes):
    account_names = []
    account_balances = []
    for account_name, account_balance in balances.items():
        account_names.append(account_name)
        account_balances.append(abs(account_balance))
    axes.pie(account_balances, labels = account_names)
