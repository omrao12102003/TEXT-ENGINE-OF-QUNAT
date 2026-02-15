import yfinance as yf
import pandas as pd
import numpy as np

def fetch_price_data(symbol_map, start_year, end_year, frequency="daily"):
    if not symbol_map:
        return pd.DataFrame()
    
    symbols = list(symbol_map.values())
    start = f"{start_year}-01-01"
    end = f"{end_year}-12-31"
    
    try:
        data = yf.download(symbols, start=start, end=end, interval="1d", progress=False)
        if len(data) > 0:
            print("Live data fetched")
            return data['Close'].dropna(how='all')
    except:
        pass
    
   
    print("Using synthetic data (network/demo mode)")
    dates = pd.date_range(start, end, freq="D")
    mock = pd.DataFrame(
        np.cumprod(1 + np.random.normal(0, 0.01, (len(dates), len(symbols))), axis=0),
        index=dates, columns=symbols
    )
    return mock.dropna()
