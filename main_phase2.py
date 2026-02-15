#!/usr/bin/env python3

from src.phase1_intent.intent_parser import IntentParser
from src.phase2_data.portfolio_engine import phase2_pipeline


def main():
    print("Quant Text Engine - Phase 1 and Phase 2")

    text = input("\nEnter request: ")

    intent_parser = IntentParser()
    intent_model = intent_parser.parse(text)

    # Pydantic V2
    intent = intent_model.model_dump()

    print("Intent Parsed Successfully")
    print("Assets:", intent["assets"])

    result = phase2_pipeline(intent)

    print("\nPHASE 2 RESULTS")
    print("Number of Assets:", len(intent["assets"]))
    print("Observations:", result["meta"]["n_obs"])
    print("Portfolio Volatility:", f"{result['portfolio_returns'].std():.4f}")
    print("Covariance Matrix Shape:", result["covariance"].shape)


if __name__ == "__main__":
    main()
