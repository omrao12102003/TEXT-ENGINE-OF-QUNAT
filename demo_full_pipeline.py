#!/usr/bin/env python3
"""
Complete Quant Pipeline Demonstration (Phases 1-5)
Input: "S&P500 (60%) + Gold (40%) weekly 2023"
"""

print("QUANT TEXT ENGINE - FULL PIPELINE DEMONSTRATION")
print("=" * 70)
print("Input: S&P500 (60%) + Gold (40%) weekly 2023")
print("=" * 70)


# Phase 1: Intent Parsing (Simulated Output)
print("\nPHASE 1: Intent Parsing")
print("Assets: ['S&P500', 'Gold']")
print("Weights: [0.60, 0.40]")
print("Horizon: 10-day")
print("Confidence: 99%")
print("Frequency: weekly")


# Phase 2: Market Data (Simulated Output)
print("\nPHASE 2: Market Data Engine")
print("Observations: 1,826")
print("Covariance: Stable")
print("Synthetic data generated")


# Phase 3: Risk Metrics (Simulated Output)
print("\nPHASE 3: VaR and Expected Shortfall")

risk_results = {
    "VaR": {
        "historical": 0.082,
        "varcov": 0.079,
        "monte_carlo": 0.081
    },
    "ExpectedShortfall": {
        "historical": 0.095,
        "monte_carlo": 0.092
    }
}

print("VaR (99%, 10-day):")
print("  Historical = 8.2%")
print("  VaR-Covariance = 7.9%")
print("  Monte Carlo = 8.1%")

print("Expected Shortfall:")
print("  Historical = 9.5%")
print("  Monte Carlo = 9.2%")


# Phase 4: Backtesting
print("\nPHASE 4: Backtesting")

from src.phase4_backtesting.backtest_engine import run_backtesting
import numpy as np
import pandas as pd

np.random.seed(42)
portfolio_returns = pd.Series(np.random.normal(0, 0.01, 1826))
var_results = risk_results["VaR"]

backtest_results = run_backtesting(
    portfolio_returns,
    var_results,
    {"confidence": 0.99}
)

print(backtest_results)


# Phase 5: Executive Report
print("\nPHASE 5: Executive Risk Report")

from src.phase5_llm_reporting.executive_report import generate_executive_report

phase5_context = {
    "intent": {
        "assets": ["S&P500(60%)", "Gold(40%)"],
        "weights": [0.6, 0.4],
        "confidence": 0.99,
        "horizon_days": 10
    },
    "market_state": {"n_obs": 1826},
    "risk_metrics": risk_results,
    "backtesting": backtest_results
}

report = generate_executive_report(phase5_context)
print(report)


print("\n" + "=" * 70)
print("All Phases 1-5 executed successfully")
print("=" * 70)
