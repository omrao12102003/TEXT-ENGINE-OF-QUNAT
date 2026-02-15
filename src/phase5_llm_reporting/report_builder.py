from .prompt_templates import EXECUTIVE_PROMPT


def build_executive_prompt(context: dict) -> str:
    intent = context["intent"]
    market = context["market_state"]
    risk = context["risk_metrics"]
    backtest = context["backtesting"]

    assets_str = ", ".join(
        f"{asset}({weight:.0%})"
        for asset, weight in zip(intent["assets"], intent["weights"])
    )

    weights_str = [f"{weight:.0%}" for weight in intent["weights"]]
    confidence_pct = int(intent["confidence"] * 100)

    kupiec_note = "Zero breaches indicate conservative calibration"

    prompt = EXECUTIVE_PROMPT.format(
        assets=assets_str,
        weights=str(weights_str),
        confidence=confidence_pct,
        horizon_days=intent["horizon_days"],
        n_obs=market["n_obs"],
        var_metrics=risk["VaR"],
        es_metrics=risk["ExpectedShortfall"],
        breaches=backtest["breaches"],
        kupiec_note=kupiec_note,
        traffic_light=backtest["traffic_light"]
    )

    return prompt


def validate_context(context: dict) -> bool:
    required_keys = ["intent", "market_state", "risk_metrics", "backtesting"]

    for key in required_keys:
        if key not in context:
            raise ValueError(f"Missing required field: {key}")

    if "VaR" not in context["risk_metrics"]:
        raise ValueError("VaR metrics are missing from risk_metrics")

    return True
