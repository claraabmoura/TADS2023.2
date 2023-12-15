import yfinance as yf 
import pandas as pd

def download_data(ticker:str) -> pd.DataFrame:
    """Download data from Yahoo Finance

    Args:
        ticker (str): _description_

    Returns:
        pd.DataFrame: _description_
    """

    data = yf.download (ticker)

    return data
