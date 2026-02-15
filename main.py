#!/usr/bin/env python3

from src.phase1_intent.intent_parser import IntentParser
from src.phase2_data.portfolio_engine import phase2_pipeline
from src.phase3_risk.risk_engine import phase3_pipeline
from src.phase4_backtesting.backtest_engine import run_backtesting
import json


def main():
    print("Quant Text Engine - Phases 1, 2, 3 and 4")

    text = input("\nEnter request: ")

    # Phase 1: Intent Parsing
    print("\nPHASE 1: Parsing")
    intent_model = IntentParser().parse(text)
    intent = intent_model.model_dump()

    print("Assets:", intent["assets"])
    print("Period:", f"{intent['start_year']} - {intent['end_year']}")

    # Phase 2: Market Engine
    print("\nPHASE 2: Market Engine")
    market_state = phase2_pipeline(intent)
    meta = market_state["meta"]

    # Phase 3: Risk Engine
    print("\nPHASE 3: Risk Engine")

    risk_config = {
        "confidence": 0.99,
        "horizon_days": 10,
        "models": ["historical", "varcov", "monte_carlo"]
    }

    risk_results = phase3_pipeline(market_state, risk_config)

    period = f"{meta.get('start_date', 'N/A')} to {meta.get('end_date', 'N/A')}"

    print("\nPipeline Results (Phases 1-3)")
    print("Assets:", intent["assets"])
    print("Weights:", intent["weights"])
    print("Observations:", meta["n_obs"])
    print("Period:", period)
    print("Covariance Matrix Shape:", market_state["covariance"].shape)

    print("\nVaR (99%, 10-day)")
    print("  Historical:", f"{risk_results['VaR']['historical']:.2%}")
    print("  VaR-Covariance:", f"{risk_results['VaR']['varcov']:.2%}")
    print("  Monte Carlo:", f"{risk_results['VaR']['monte_carlo']:.2%}")

    print("\nExpected Shortfall")
    print("  Historical:", f"{risk_results['ExpectedShortfall']['historical']:.2%}")
    print("  Monte Carlo:", f"{risk_results['ExpectedShortfall']['monte_carlo']:.2%}")

    # Phase 4: Backtesting
    print("\nPHASE 4: Backtesting and Validation")

    backtest_results = run_backtesting(
        market_state["portfolio_returns"],
        risk_results["VaR"],
        {
            "confidence": risk_config["confidence"],
            "horizon_days": risk_config["horizon_days"]
        }
    )

    print("\nBacktest Summary:")
    print(json.dumps(backtest_results, indent=2, default=str))

    print("Traffic Light:", backtest_results["traffic_light"])

    print("\nPipeline execution completed successfully.")


if __name__ == "__main__":
    main()
