import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller


def train_val_test_split(df, train_rate, val_rate, shuffle=False):
    '''
    for data in df, perform train, validation, and test split
    '''
    n = len(df)
    if shuffle == True:
        df = df.sample(n)
    
    train_index = int(n * train_rate)
    val_index = train_index + int(n * val_rate)
    
    df_train = df[:train_index]
    df_val = df[train_index: val_index]
    df_test = df[val_index:]
    
    return df_train, df_val, df_test
    
    
def plot_train_val_test(df_train, df_val, df_test, ax):
    
    if df_train is not None:
        ax.plot(df_train, color='red', label="train")
    if df_val is not None:
        ax.plot(df_val, color='green', label="validation")
    if df_test is not None:
        ax.plot(df_test, color='blue', label="test")
    
    ax.legend(loc='upper left', fontsize=10)
    
    
def plot_moving_average(series, window, ax, plot_actual=False, scale=1.96):

    rolling_mean = series.rolling(window=window).mean()

    ax.set_title("Moving average\n window size = {}".format(window))
    ax.plot(rolling_mean, "g", label="Rolling mean trend")
    
    if plot_actual:
        ax.plot(series[window:], label="Actual values")
        
    ax.legend(loc="upper left") 
    ax.grid()
    
    
def difference_series_n(timeseries, n, lag):
    
    for i in range(n):
        timeseries = differece_series(timeseries, lag)
    return timeseries


def differece_series(timeseries, lag):
    n = len(timeseries)
    A = timeseries[lag:n]
    B = timeseries[0:n-lag]
    
    return A-B


def min_diff_times(timeseries, lag=1, p_value=0.05):
    p = adfuller(timeseries, autolag='AIC')[1]
    n = 0
    
    while p > p_value:
        print(f"Difference data {n} times, p value = {p}")
        timeseries = differece_series(timeseries, lag)
        p = adfuller(timeseries, autolag='AIC')[1]
        n += 1
        
    print(f"Difference data {n} times, p value = {p}")
    return n, timeseries