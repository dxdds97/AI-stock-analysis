import yfinance as yf
import pandas as pd

def load_stock_data(ticker, period="1y", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval, proxy=None, auto_adjust=False)
    data.dropna(inplace=True)
    return data