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
    return sorted(ledger, key=lambda d: d['date'])


def check_entries_sum(ledger):
    '''
    Check entries in a transaction sum to zero.

    Parameters
    ----------
    Ledger : dict
        Loaded json file.

    Returns
    -------
    Print statement
        A statement is printed to inform the user if the entries sum to zero or not.
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
        raise Warning("Entries do not sum to zero, but ", amount_sum)
