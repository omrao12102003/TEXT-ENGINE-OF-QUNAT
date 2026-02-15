import numpy as np
import pandas as pd
def compute_portfolio_returns(returns_df, weights):
    if len(returns_df) == 0: return pd.Series()
    return returns_df.dot(np.array(weights))

def compute_covariance(returns_df):
    if len(returns_df) == 0: return pd.DataFrame()
    return returns_df.cov()

def phase2_pipeline(intent):
    from .market_mapper import map_assets
    from .data_fetcher import fetch_price_data
    from .data_cleaner import clean_prices
    from .returns_engine import compute_log_returns
    prices = fetch_price_data(map_assets(intent['assets']), intent['start_year'], intent['end_year'], intent['data_frequency'])
    prices = clean_prices(prices)
    returns = compute_log_returns(prices)
    port_returns = compute_portfolio_returns(returns, intent['weights'])
    return {
        "returns": returns,
        "portfolio_returns": port_returns,
        "covariance": compute_covariance(returns),
        "meta": {"n_obs": len(returns), "symbols": map_assets(intent['assets'])}
    }
