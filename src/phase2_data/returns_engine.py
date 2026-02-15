import numpy as np
import pandas as pd
def compute_log_returns(df):
    if len(df) == 0: return df
    return np.log(df / df.shift(1)).dropna()
