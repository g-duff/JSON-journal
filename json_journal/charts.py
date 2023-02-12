'''Create charts'''
import numpy as np

def create_pie_chart(balances, axes):
    '''
    Create a pie chart on given axes.

    Parameters
    ----------
    Balances : dict
        Full account names and balances for each account.
    Axes : int
        Specifed axes for plotting the pie chart.
    '''
    account_names = []
    account_balances = []
    for account_name, account_balance in balances.items():
        account_names.append(account_name)
        account_balances.append(abs(account_balance))
    axes.pie(account_balances, labels=account_names)


def create_line_graph(cumulative_profit, axes):
    '''
    Create a line graph on given axes.

    Parameters
    ----------
    Cumulative_profit : tuple
        Contains a list for the x axis (dates) and a list for the y axis (profits).
    Axes : int
        Specifed axes for plotting the line graph.
    '''
    dates, profits = cumulative_profit
    axes.plot([np.datetime64(d) for d in dates], profits)
