import pandas as pd
from .breach_detector import count_var_breaches
from .kupiec_test import kupiec_test
from .traffic_light import traffic_light

def run_backtesting(portfolio_returns: pd.Series, var_results: dict, risk_config: dict):
    """
    Phase 4: breaches -> Kupiec -> Traffic Light.
    Now correctly matches VaR horizon with rolling returns.
    """

    confidence = risk_config["confidence"]
    horizon = risk_config["horizon_days"]

    # ✅ Create rolling horizon returns (log returns add)
    rolling_returns = portfolio_returns.rolling(horizon).sum().dropna()

    n_obs = len(rolling_returns)

    results = {
        "breaches": {},
        "kupiec": {},
        "traffic_light": {},
        "meta": {
            "confidence": confidence,
            "horizon_days": horizon,
            "n_obs": n_obs
        }
    }

    for model, var_value in var_results.items():

        breaches_count, _ = count_var_breaches(rolling_returns, var_value)

        results["breaches"][model] = int(breaches_count)

        if n_obs > 0:
            results["kupiec"][model] = kupiec_test(
                breaches_count,
                n_obs,
                confidence
            )
            results["traffic_light"][model] = traffic_light(
                breaches_count,
                n_obs
            )
        else:
            results["kupiec"][model] = {"LR": None, "p_value": None, "pass": False}
            results["traffic_light"][model] = "No Data"
    
    return results
