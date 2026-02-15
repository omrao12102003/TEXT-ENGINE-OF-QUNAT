import numpy as np
import pandas as pd

def historical_var(portfolio_returns: pd.Series, confidence: float, horizon_days: int) -> float:
    """
    Historical Simulation VaR: empirical quantile scaling.
    VaR_α = Quantile_(1-α)(R_p) * √h
    """
    if len(portfolio_returns) == 0:
        return 0.0
    
    scaled_returns = portfolio_returns * np.sqrt(horizon_days)
    var_value = -np.quantile(scaled_returns, 1 - confidence)
    return float(var_value)
