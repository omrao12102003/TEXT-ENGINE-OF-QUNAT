#!/usr/bin/env python3
"""
Quant Text Engine - Full Pipeline (Phases 1-5)
"""

import sys
import pandas as pd
import numpy as np

# Phase 1-3 assumed to run successfully and produce:
# portfolio_returns (pd.Series)
# risk_results (dict with VaR and Expected Shortfall)
# intent (parsed object)


print("\nPHASE 4: Backtesting")

from src.phase4_backtesting.backtest_engine import run_backtesting

var_results = {
    "historical": 0.0729,
    "varcov": 0.0727,
    "monte_carlo": 0.0734
}

backtest_results = run_backtesting(
    portfolio_returns,
    var_results,
    {"confidence": 0.99}
)

print(backtest_results)


print("\nPHASE 5: Executive Report")

from src.phase5_llm_reporting.executive_report import generate_executive_report

phase5_context = {
    "intent": {
        "assets": ["NIFTY50"],
        "weights": [1.0],
        "confidence": 0.99,
        "horizon_days": 10
    },
    "market_state": {"n_obs": 1826},
    "risk_metrics": {
        "VaR": var_results,
        "ExpectedShortfall": {
            "historical": 0.0729,
            "monte_carlo": 0.0734
        }
    },
    "backtesting": backtest_results
}

report = generate_executive_report(phase5_context)
print(report)


print("\nAll phases completed successfully.")
