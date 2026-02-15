#!/usr/bin/env python3
"""
End-to-End Quant Pipeline: Input to Phases 1-5 Output
"""

import numpy as np
import pandas as pd


# Simulated Phases 1-3
def run_phases_1_to_3(user_input: str):
    print("PHASE 1: Parsing")
    print("Input:", user_input)

    # Simulated Phase 2-3 outputs
    portfolio_returns = pd.Series(
        np.random.normal(0, 0.01, 1826)
    )

    risk_results = {
        "VaR": {
            "historical": 0.0746,
            "varcov": 0.0731,
            "monte_carlo": 0.0740
        },
        "ExpectedShortfall": {
            "historical": 0.0912,
            "monte_carlo": 0.0898
        }
    }

    return portfolio_returns, risk_results


# Phase 4: Backtesting
def run_phase_4(portfolio_returns, risk_results):
    from src.phase4_backtesting.backtest_engine import run_backtesting

    var_results = {
        key: abs(value)
        for key, value in risk_results["VaR"].items()
    }

    return run_backtesting(
        portfolio_returns,
        var_results,
        {"confidence": 0.99}
    )


# Phase 5: Executive Report
def run_phase_5(risk_results, backtest_results):
    from src.phase5_llm_reporting.executive_report import generate_executive_report

    context = {
        "intent": {
            "assets": ["Portfolio"],
            "weights": [1.0],
            "confidence": 0.99,
            "horizon_days": 10
        },
        "market_state": {"n_obs": 1826},
        "risk_metrics": risk_results,
        "backtesting": backtest_results
    }

    return generate_executive_report(context)


# Main Execution
def main():
    user_input = input("Enter request: ").strip()

    print("\nFULL PIPELINE EXECUTION")

    portfolio_returns, risk_results = run_phases_1_to_3(user_input)
    print("\nPhases 1-3 completed: VaR and ES calculated")

    backtest_results = run_phase_4(portfolio_returns, risk_results)
    print("\nPHASE 4: Backtesting completed")
    print("Traffic Light:", backtest_results["traffic_light"])

    report = run_phase_5(risk_results, backtest_results)
    print("\nPHASE 5: Executive Report")
    print(report)

    print("\nPipeline execution completed successfully.")


if __name__ == "__main__":
    main()
