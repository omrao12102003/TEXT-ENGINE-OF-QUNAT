#!/usr/bin/env python3
"""
Phase 5 Standalone Test - Executive Reporting
"""

from src.phase5_llm_reporting.executive_report import generate_executive_report
from src.phase5_llm_reporting.report_builder import validate_context

test_context = {
    "intent": {
        "assets": ["NIFTY50"],
        "weights": [1.0],
        "confidence": 0.99,
        "horizon_days": 10
    },
    "market_state": {
        "n_obs": 1826,
        "frequency": "daily"
    },
    "risk_metrics": {
        "VaR": {
            "historical": 0.0746,
            "varcov": 0.0731,
            "monte_carlo": 0.0740
        },
        "ExpectedShortfall": {
            "historical": 0.0912,
            "monte_carlo": 0.0898
        }
    },
    "backtesting": {
        "breaches": {
            "historical": 0, 
            "varcov": 0,
            "monte_carlo": 0
        },
        "kupiec": {
            "historical": {"LR": float("inf"), "p_value": 0.0, "pass": False},
            "varcov": {"LR": float("inf"), "p_value": 0.0, "pass": False},
            "monte_carlo": {"LR": float("inf"), "p_value": 0.0, "pass": False}
        },
        "traffic_light": {
            "historical": "Green",
            "varcov": "Green", 
            "monte_carlo": "Green"
        }
    }
}

print(" PHASE 5 STANDALONE TEST")
print("=" * 50)

try:
    validate_context(test_context)
    report = generate_executive_report(test_context)
    print(report)
    print("\n PHASE 5: EXECUTIVE REPORTING VALIDATED ")
except Exception as e:
    print(f" Phase 5 failed: {e}")
