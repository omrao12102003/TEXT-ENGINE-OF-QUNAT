from .llm_client import LLMClient
from .report_builder import build_executive_prompt, validate_context


def generate_executive_report(context: dict) -> str:
    """
    Generates an executive-level risk report based on processed context.
    """

    validate_context(context)

    prompt = build_executive_prompt(context)

    llm = LLMClient()
    report = llm.generate(prompt)

    return report


def generate_full_risk_memo(context: dict) -> dict:
    """
    Returns the executive report along with basic metadata.
    """

    report = generate_executive_report(context)

    return {
        "timestamp": "2026-02-08",
        "portfolio": context["intent"]["assets"],
        "confidence": context["intent"]["confidence"],
        "executive_summary": report,
        "phase_validation": "Phases 1-5 COMPLETE"
    }
