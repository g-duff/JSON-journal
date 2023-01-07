from json_journal import data_analysis
from json_journal import file_io
from json_journal import organise_data
from json_journal import tabulate_data



if __name__ == '__main__':

    json_file = 'finances.json'
    ledger = file_io.load_json_file(json_file)

    entries = organise_data.separate_out_entities(ledger)
    expenses = organise_data.separate_expenses(entries)
    file_io.save_json_file(expenses, "json_files/expenses.json")

    file_io.save_json_file(entries, "json_files/balance.json")
    balances = organise_data.separate_main_accounts(entries)
    sorted_accounts = sorted(balances.keys())
    tabulate_data.tabulate_sorted_entries(balances, sorted_accounts)
    print("Total =", data_analysis.total_profit(entries))
