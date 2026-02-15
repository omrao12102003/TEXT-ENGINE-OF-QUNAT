import numpy as np
from scipy.stats import chi2

def kupiec_test(num_breaches: int, n_obs: int, confidence: float = 0.99):
    """
    Kupiec LR_uc test for unconditional coverage.
    H0: breach prob = 1-confidence. Pass if p>0.05.
    """
    p = 1 - confidence
    phat = num_breaches / n_obs if n_obs > 0 else 0

    if phat == 0 or phat == 1:
        return {"LR": np.inf, "p_value": 0.0, "pass": False}

    num_good = n_obs - num_breaches
    LR = -2 * np.log(
        ((1 - p) ** num_good * p ** num_breaches) /
        ((1 - phat) ** num_good * phat ** num_breaches)
    )

    p_value = 1 - chi2.cdf(LR, df=1)
    return {
        "LR": float(LR),
        "p_value": float(p_value),
        "pass": p_value > 0.05
    }
