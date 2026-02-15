EXECUTIVE_PROMPT = """
Prepare an internal risk memorandum based on the following portfolio information.

Portfolio Details:
Assets: {assets}
Weights: {weights}
Confidence Level: {confidence}%
Time Horizon: {horizon_days}-day
Number of Observations: {n_obs:,} trading days

Risk Metrics:
VaR Estimates:
  Historical = {var_metrics[historical]:.1%}
  VaR-Covariance = {var_metrics[varcov]:.1%}
  Monte Carlo = {var_metrics[monte_carlo]:.1%}

Expected Shortfall:
  Historical = {es_metrics[historical]:.1%}
  Monte Carlo = {es_metrics[monte_carlo]:.1%}

Backtesting Results:
Breaches:
  Historical = {breaches[historical]}
  VaR-Covariance = {breaches[varcov]}
  Monte Carlo = {breaches[monte_carlo]}

Kupiec Test Result: {kupiec_note}
Traffic Light Classification: {traffic_light}

Instructions:
1. Provide a one-sentence summary of overall portfolio risk.
2. Comment on consistency between risk models.
3. Interpret backtesting performance with respect to regulatory standards.
4. Provide a clear recommendation for risk monitoring.

Format the response using the following section headings:

EXECUTIVE RISK SUMMARY:
MODEL RELIABILITY ASSESSMENT:
TAIL RISK INTERPRETATION:
REGULATORY STATUS:
CRO RECOMMENDATION:

Keep the tone formal and concise. Limit each section to a maximum of four sentences.
"""
