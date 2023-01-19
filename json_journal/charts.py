'''Create charts'''


def create_pie_chart(balances, axes):
    '''
    Create a pie chart on given axes.

    Parameters
    ----------
    Balances : dict
        Full account names and balances for each account.
    Axes : int
        Specifed axes for plotting the pie chart.

    Returns
    -------
    Pie chart ready to be shown (n.b. plt.show needs to be called on this pie chart)
    '''
    account_names = []
    account_balances = []
    for account_name, account_balance in balances.items():
        account_names.append(account_name)
        account_balances.append(abs(account_balance))
    axes.pie(account_balances, labels=account_names)

def create_line_graph(monthly_profit, axes):
    dates = []
    profits = []
    for date, profit in monthly_profit.items():
        dates.append(date)
        profits.append(profit)
    axes.plot(dates, profits)