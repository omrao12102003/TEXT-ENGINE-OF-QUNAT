import pandas as pd
import numpy as np
import json
from src.phase4_backtesting.backtest_engine import run_backtesting

# Mock Phase 3 output (synthetic data like your Phase 2)
portfolio_returns = pd.Series(np.random.normal(0, 0.01, 1826))  # Matches your n_obs
var_results = {
    "historical": 0.0746,
    "varcov": 0.0731, 
    "monte_carlo": 0.0740
}
risk_config = {"confidence": 0.99, "horizon_days": 10}

# Run Phase 4
backtest_results = run_backtesting(portfolio_returns, var_results, risk_config)

print("PHASE 4 done")
print(json.dumps(backtest_results, indent=2))
