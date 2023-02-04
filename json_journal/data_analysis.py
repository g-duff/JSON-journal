'''Functions for various analysis on data'''

ACCOUNT_NAME_SEPARATOR = ':'


def calculate_balance(ledger):
    '''
    Calculate balance for all entries.

    Parameters
    ----------
    Ledger : dict
        Loaded json file.

    Returns
    -------
    All_balances : dict
        Contains full account names and balances for each account.
    '''
    all_balances = {}
    for transaction in ledger:
        entries = transaction['entries']

        for entry in entries:
            amount = entry['amount']
            account = entry['account']

            if account in all_balances:
                new_amount = amount + all_balances.get(account)
                all_balances[account] = new_amount
            else:
                all_balances[account] = amount
    return all_balances


def parent_account_balances(full_account_name_balances):
    '''
    Calculate balances for all parent accounts.

    Parameters
    ----------
    Full_account_name_balances : dict
        Contains the full account name and corresponding balance.

    Returns
    -------
    New_balances : dict
        Contains balances for each parent account.
    '''
    new_balances = {}
    for full_account_name in full_account_name_balances.keys():
        account_separated = full_account_name.split(ACCOUNT_NAME_SEPARATOR)
        for child_account_name in range(len(account_separated)):
            parent_account = ACCOUNT_NAME_SEPARATOR.join(
                account_separated[:child_account_name+1])
            if parent_account in new_balances:
                new_balances[parent_account] += full_account_name_balances[full_account_name]
            else:
                new_balances[parent_account] = full_account_name_balances[full_account_name]
    return new_balances


def total_profit(full_account_name_balances):
    '''
    Calculate the total profit.

    Parameters
    ----------
    Full_account_name_balances : dict
        Contains the full account name and corresponding balance.

    Returns
    -------
    Total : int
        Total profit value.
    '''
    expenses = 0
    income = 0
    for account in full_account_name_balances:
        if account.startswith("expense:"):
            expenses += full_account_name_balances[account]
        if account.startswith("income:"):
            income += full_account_name_balances[account]
        else:
            pass
    total = (income * (-1)) - expenses
    return total


def calculate_profit(ledger):
    '''
    Calculate the profit of a ledger file.

    Parameters
    ----------
    Ledger : list of dicts
        Loaded json file.

    Returns
    -------
    Profit_calculated : int
        Value of total profit.
    '''
    profit_sorted_ledger = sorted(ledger, key=lambda d: d['date'])
    profit_calculated = 0
    for transaction in profit_sorted_ledger:
        entries = transaction['entries']
        for entry in entries:
            amount = entry['amount']
            account = entry['account']
            if account.startswith("expense:"):
                profit_calculated -= amount
            elif account.startswith("income"):
                profit_calculated += (-1) * amount
    return profit_calculated



def cumulative_profit(ledger):
    '''
    Calculate the cumulative profit.

    Parameters
    ----------
    Ledger : list of dicts
        Loaded json file.

    Returns
    -------
    Dates : list
        List of dates.
    Cumulative_profits : list
        List of cumulative total of profit.
    '''
    sorted_ledger = sorted(ledger, key=lambda d: d['date'])

    dates = [sorted_ledger[0]['date']]
    cumulative_profits = [calculate_profit(sorted_ledger[0:1])]

    for transaction in sorted_ledger[1:]:
        entries = transaction['entries']
        profit = 0
        for entry in entries:
            amount = entry['amount']
            account = entry['account']
            if account.startswith("expense:"):
                profit -= amount
            elif account.startswith("income"):
                profit += ((-1) * amount)

        transaction_date = transaction['date']
        if transaction_date == dates[-1]:
            cumulative_profits[-1] += profit
        else:
            dates.append(transaction_date)
            cumulative_profits.append(cumulative_profits[-1] + profit)

    return dates, cumulative_profits
