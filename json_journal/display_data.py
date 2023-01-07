from tabulate import tabulate

def tabulate_sorted_entries(all_entries, sorted_accounts):
        output_rows = [[i, all_entries[i]] for i in sorted_accounts]
        output_headers = ["Account", "Amount"]
        print(tabulate(output_rows, headers=output_headers))