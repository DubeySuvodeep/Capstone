import os, sys
import yfinance as yf
# import ta
import pandas as pd
import numpy as np
import vectorbt as vbt
from datetime import date, timedelta, datetime
from itertools import product
from IPython.display import clear_output
import matplotlib.pyplot as mp
from csv import writer
import warnings

# Settings the warning to be ignored
warnings.filterwarnings('ignore')


def execute_main():
    # dt_range = pd.date_range('2019-12-31', '2020-12-31', freq='6m') 
    # define start and end date
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    # extract data from yahoo finanace
    btc_price = vbt.YFData.download(
    ["BTC-USD", "ETH-USD", "XMR-USD", "ADA-USD"],
    interval='1m',
    start = start_date,
    end = end_date,
    missing_index='drop').get("Close")

    # Initialize a Indicator Factory using custom indicator
    # Step2. Receipe how to create an indicator
    ind = vbt.IndicatorFactory(
        class_name = "Combination",
        short_name = "comb",
        input_names = ["close"],
        param_names = ["rsi_window", "ma_window"],
        output_names = ["value"]
    ).from_apply_func(
        custom_indicator,
        rsi_window=14,
        ma_window=50
    )

    # Step3. execute the custom indicator with the given parameters
    res = ind.run(
        btc_price,
        rsi_window=21,
        ma_window=50
    )

    # Results
    for _col in res.value.columns:
        print("-------------------{}------------------------------".format(_col))
        _asset = res.value[_col].to_numpy()
        _entry = np.where(_asset==1, True, False)
        _exit = np.where(_asset==-1, True, False)
        
        pf = vbt.Portfolio.from_signals(btc_price[_col[2]], _entry, _exit)
        print(pf.stats())
        pf.plot(title=_col[2]).show()
        print("----------------------------------------------------------")


# Step 1. Create a custom indicator
def custom_indicator(close, rsi_window=14, ma_window=50):
    rsi = vbt.RSI.run(close, window=rsi_window).rsi.to_numpy()
    ma = vbt.MA.run(close, ma_window).ma.to_numpy()
    # we will create a signal
    # For example rsi between 35 and 70, and price will be above ma,we will buy
    trend = np.where(rsi>70, -1, 0)
    trend = np.where((rsi<30) & (close < ma), 1, trend)
    return trend

if __name__=="__main__":
    execute_main()