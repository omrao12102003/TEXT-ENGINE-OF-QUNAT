import numpy as np
import pandas as pd
from typing import Dict, Any

from .historical_var import historical_var
from .varcov_var import varcov_var
from .monte_carlo_var import monte_carlo_var
from .expected_shortfall import expected_shortfall

def phase3_pipeline(market_state: Dict[str, Any], risk_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Phase 3 Contract: market_state → risk metrics.
    Input from Phase 2, config from Phase 1 intent.
    """
    portfolio_returns = market_state["portfolio_returns"]
    
    confidence = risk_config.get("confidence", 0.99)
    horizon_days = risk_config.get("horizon_days", 10)
    models = risk_config.get("models", ["historical", "varcov", "monte_carlo"])
    
    results = {
        "VaR": {},
        "ExpectedShortfall": {},
        "meta": {
            "confidence": confidence,
            "horizon_days": horizon_days,
            "n_obs": len(portfolio_returns),
            "models": models
        }
    }
    
    # Historical
    if "historical" in models:
        var_hist = historical_var(portfolio_returns, confidence, horizon_days)
        results["VaR"]["historical"] = var_hist
        results["ExpectedShortfall"]["historical"] = expected_shortfall(
            portfolio_returns, var_hist, confidence
        )
    
    # Var-Cov
    if "varcov" in models:
        results["VaR"]["varcov"] = varcov_var(portfolio_returns, confidence, horizon_days)
    
    # Monte Carlo
    if "monte_carlo" in models:
        var_mc = monte_carlo_var(portfolio_returns, confidence, horizon_days)
        results["VaR"]["monte_carlo"] = var_mc
        results["ExpectedShortfall"]["monte_carlo"] = expected_shortfall(
            portfolio_returns, var_mc, confidence
        )
    
    return results
