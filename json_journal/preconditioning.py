'''Data sorted before being used by analysis'''

def sort_journal_by_date(ledger):
    '''
    Sort JSON file by date.

    Parameters
    ----------
    Ledger : dict
        Loaded json file.

    Returns
    -------
    Sorted_ledger : dict
        The same json file, ordered by date.
    '''
    sorted_ledger = sorted(ledger, key=lambda d: d['date'])
    return sorted_ledger


def check_entries_sum(ledger):
    '''
    Check entries in a transaction sum to zero.

    Parameters
    ----------
    Ledger : dict
        Loaded json file.

    Returns
    -------
    Amount_sum : int
        The sum of entry amounts in each transaction.
    '''
    amount_sum = 0
    for transaction in ledger:
        entries = transaction['entries']


        for entry in entries:
            amount = entry['amount']
            amount_sum += amount
    
    if amount_sum == 0:
        print("Entries sum to zero")
    else:
        print("Entries do not sum to zero, but ", amount_sum)

