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




