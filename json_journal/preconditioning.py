'''Data sorted before being used by analysis'''


def sort_journal_by_date(ledger):
    '''
    Sort dictionary by date.

    Parameters
    ----------
    Ledger : dict
        Dictionary with dates, descriptions and entries.

    Returns
    -------
    Sorted_ledger : dict
        Dictionary sorted by date with descriptions and entries.
    '''
    return sorted(ledger, key=lambda d: d['date'])


def check_entries_sum_to_zero(ledger):
    '''
    Check entries in a transaction sum to zero.

    Parameters
    ----------
    Ledger : dict
        Dictionary with dates, descriptions and entries.

    Returns
    -------
    Amount_sum : int
        The value of the total sum of entries in the ledger. NB this is to use in tests.
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
    return amount_sum
