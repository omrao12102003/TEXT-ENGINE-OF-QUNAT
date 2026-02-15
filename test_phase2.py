from src.phase1_intent.intent_parser import IntentParser
from src.phase2_data.portfolio_engine import phase2_pipeline
intent = IntentParser().parse('NIFTY50 (100%) daily 2024').model_dump()
result = phase2_pipeline(intent)
print("PHASE 2:", result['meta'])
