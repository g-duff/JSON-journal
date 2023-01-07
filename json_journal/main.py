from matplotlib import pyplot as plt
from json_journal import charts
from json_journal import data_analysis
from json_journal import file_io
from json_journal import filters
from json_journal import tabulate_data



if __name__ == '__main__':

    personal_finance_directory = "../Prod/"

    ledger_filepath = personal_finance_directory + "finances.json"
    expenses_filepath = personal_finance_directory + "expenses.json"
    balance_filepath = personal_finance_directory + "balance.json"
    
    ledger = file_io.load_json_file(ledger_filepath)

    full_account_name_balance = data_analysis.calculate_balance(ledger)
    expenses = filters.filter_balances_to_expenses(full_account_name_balance)
    file_io.save_json_file(expenses, expenses_filepath)

    file_io.save_json_file(full_account_name_balance, balance_filepath)
    parent_account_name_balances = data_analysis.parent_account_balances(full_account_name_balance)
    sorted_accounts = sorted(parent_account_name_balances.keys())
    tabulate_data.tabulate_sorted_entries(parent_account_name_balances, sorted_accounts)
    print("Total =", data_analysis.total_profit(full_account_name_balance))

    fig, (left_axes, right_axes) = plt.subplots(ncols=2)
    charts.create_pie_chart(full_account_name_balance, left_axes)
    charts.create_pie_chart(expenses, right_axes)
    plt.show()
