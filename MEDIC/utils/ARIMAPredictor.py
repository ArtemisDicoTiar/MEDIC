import sys
import warnings

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.optimize import brute
from statsmodels.tsa.arima.model import ARIMA

warnings.simplefilter("ignore", category='UserWarning')


def objfunc(order, endog):
    try:
        fit = ARIMA(endog=endog, order=order).fit()
        return fit.aic
    except:
        return sys.maxsize


def get_arima_predictions(pd_df: pd.DataFrame,
                          target_case: str,
                          pred_periods: int):

    grid = (slice(1, 3, 1), slice(1, 3, 1), slice(1, 3, 1))
    res = brute(objfunc, grid,
                args=([np.asarray(pd_df[target_case], dtype='float64')]),
                finish=None)

    mod = sm.tsa.arima.ARIMA(np.asarray(pd_df[target_case], dtype='float64'), order=res)
    res = mod.fit(low_memory=True)
    pred = res.predict(start=len(pd_df)+1, end=len(pd_df)+pred_periods).astype(np.int64)

    return pred
