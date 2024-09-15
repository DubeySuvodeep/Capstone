import pandas as pd 
import yfinance as yf 

class YahooFin:

    def __init__(self, ticker):
        self.historical_stock_price = None
        self.ticker = ticker
        self.price = None
        self.start_date = "2019-01-01"
        self.end_date = "2022-12-31"

    # fetching past data from the yahoo finance
    def get_data(self):
        try:
            if type(self.ticker)!=list:
                self.ticker = [self.ticker]

            self.historical_stock_price = yf.download(self.ticker, start=self.start_date, end=self.end_date, interval="1d")
            self.price = self.historical_stock_price['Adj Close']
            # self.price.index = pd.to_datetime(self.historical_stock_price.index, format="%y%m%d")
        except Exception as err:
            print(err)            
