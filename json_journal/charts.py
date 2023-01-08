'''Create pie chart'''

def create_pie_chart(balances, axes):
    '''balances -> dictionary of full account names and balances for each account,
    axes -> specifed axes for plotting the pie chart.
    Returns pie chart ready to be shown (n.b. plt.show needs to be called on this pie chart)'''
    account_names = []
    account_balances = []
    for account_name, account_balance in balances.items():
        account_names.append(account_name)
        account_balances.append(abs(account_balance))
    axes.pie(account_balances, labels=account_names)
