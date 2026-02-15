import pandas as pd

def count_var_breaches(portfolio_returns: pd.Series, var_value: float):
    """
    Count breaches: realized return < -VaR (loss exceeds threshold).
    Returns (count, boolean Series for analysis).
    """
    breaches = portfolio_returns < -var_value
    return int(breaches.sum()), breaches

