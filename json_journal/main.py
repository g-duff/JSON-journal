from json_journal import file_io
from json_journal import display_data
from json_journal import organise_data
from json_journal import data_analysis


if __name__ == '__main__':

    json_file = 'finances.json'
    entries = {}
    ledger = file_io.load_json_file(json_file)

    organise_data.separate_out_entities(ledger, entries)
    expenses = organise_data.separate_expenses(entries)
    file_io.save_expenses_as_json(expenses)

    file_io.save_all_balances_as_json(entries)
    balances = organise_data.separate_main_accounts(entries)
    sorted_accounts = sorted(balances.keys())
    display_data.tabulate_sorted_entries(balances, sorted_accounts)
    print("Total =", data_analysis.total_profit(entries))
