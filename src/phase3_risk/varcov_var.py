import numpy as np
import pandas as pd
from scipy.stats import norm

def varcov_var(portfolio_returns: pd.Series, confidence: float, horizon_days: int) -> float:
    """
    Parametric VaR under normal assumption.
    Returns positive loss magnitude.
    """

    if len(portfolio_returns) == 0:
        return 0.0

    mu = portfolio_returns.mean()
    sigma = portfolio_returns.std()
    z = norm.ppf(confidence)

    # Standard parametric VaR (positive magnitude)
    var_value = z * sigma * np.sqrt(horizon_days) - mu * horizon_days

    return float(abs(var_value))
