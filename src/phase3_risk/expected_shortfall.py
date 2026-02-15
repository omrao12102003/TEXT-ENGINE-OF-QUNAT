import numpy as np
import pandas as pd

def expected_shortfall(portfolio_returns: pd.Series, var_value: float, 
                      confidence: float) -> float:
    """
    Expected Shortfall (CVaR): average loss beyond VaR threshold.
    ES_α = E[R | R ≤ VaR_α]
    """
    if len(portfolio_returns) == 0:
        return 0.0
    
    # Losses beyond VaR threshold
    tail_losses = portfolio_returns[portfolio_returns <= -var_value]
    
    if len(tail_losses) == 0:
        return float(var_value)  # Conservative fallback
    
    es_value = -tail_losses.mean()
    return float(es_value)
