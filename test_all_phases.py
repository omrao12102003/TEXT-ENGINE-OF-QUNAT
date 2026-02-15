#!/usr/bin/env python3
"""
Full Pipeline Test: Phases 1-5 Demonstration
Test Input: "S&P500 (60%) + Gold (40%) weekly 2023"
"""

import sys
from io import StringIO


def main():
    # Mock input for main.py (Phases 1-3)
    original_stdin = sys.stdin
    sys.stdin = StringIO("S&P500 (60%) + Gold (40%) weekly 2023\n")

    # Execute main.py (assumes it defines portfolio_returns)
    exec(open("main.py").read())

    # Restore stdin
    sys.stdin = original_stdin

    print("\n" + "=" * 80)
    print("PHASE 4: Backtesting Validation")
    print("=" * 80)

    from src.phase4_backtesting.backtest_engine import run_backtesting

    var_results = {
        "historical": 0.082,
        "varcov": 0.079,
        "monte_carlo": 0.081
    }

    backtest_results = run_backtesting(
        portfolio_returns,
        var_results,
        {"confidence": 0.99}
    )

    print(backtest_results)

    print("\n" + "=" * 80)
    print("PHASE 5: Executive Risk Memo")
    print("=" * 80)

    from src.phase5_llm_reporting.executive_report import generate_executive_report

    phase5_context = {
        "intent": {
            "assets": ["S&P500(60%)", "Gold(40%)"],
            "weights": [0.6, 0.4],
            "confidence": 0.99,
            "horizon_days": 10
        },
        "market_state": {"n_obs": 1826},
        "risk_metrics": {
            "VaR": var_results,
            "ExpectedShortfall": {
                "historical": 0.095,
                "monte_carlo": 0.092
            }
        },
        "backtesting": backtest_results
    }

    report = generate_executive_report(phase5_context)
    print(report)

    print("\n" + "=" * 80)
    print("All Phases 1-5 executed successfully.")
    print("=" * 80)


if __name__ == "__main__":
    main()
