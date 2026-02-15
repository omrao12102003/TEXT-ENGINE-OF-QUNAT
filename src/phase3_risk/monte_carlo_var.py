import numpy as np
import pandas as pd

def monte_carlo_var(portfolio_returns: pd.Series, confidence: float, 
                   horizon_days: int, simulations: int = 10000) -> float:
    """
    Monte Carlo VaR: simulate normal paths.
    R_sim ~ N(μh, σ√h)
    """
    if len(portfolio_returns) == 0:
        return 0.0
    
    mu = portfolio_returns.mean()
    sigma = portfolio_returns.std()
    
    sim_returns = np.random.normal(
        mu * horizon_days,
        sigma * np.sqrt(horizon_days),
        simulations
    )
    
    var_value = -np.quantile(sim_returns, 1 - confidence)
    return float(var_value)
