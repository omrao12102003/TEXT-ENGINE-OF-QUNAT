from src.phase1_intent.intent_parser import IntentParser
from src.phase2_data.portfolio_engine import phase2_pipeline
from src.phase3_risk.risk_engine import phase3_pipeline

# Phase 1+2
intent = IntentParser().parse("NIFTY50 (100%) daily 2024").model_dump()
market_state = phase2_pipeline(intent)

# Phase 3
risk_config = {
    "confidence": 0.99,
    "horizon_days": 10,
    "models": ["historical", "varcov", "monte_carlo"]
}

risk_results = phase3_pipeline(market_state, risk_config)

print("PHASE 3 done")
print("Market State:", market_state["meta"])
print("Risk Results:", risk_results)
