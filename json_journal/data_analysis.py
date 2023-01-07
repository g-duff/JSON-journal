def total_profit(all_balances):
    expenses = 0
    income = 0
    for account in all_balances: 
        if account.startswith("expense:"):
            expenses += all_balances[account]
        else:
            pass
    for account in all_balances: 
        if account.startswith("income:"):
            income += all_balances[account]
        else:
            pass
    total = (income * (-1)) - expenses
    return total