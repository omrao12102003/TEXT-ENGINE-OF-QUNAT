import pandas as pd
def clean_prices(df):
    if len(df) == 0: return df
    df = df.ffill().bfill().dropna()
    return df
