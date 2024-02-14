import datetime as dt

import matplotlib.pyplot as plt

import matplotlib.ticker as mtick

import numpy as np

import pandas as pd

import yfinance as yf


DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:

    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        """method that downloads data and stores in a DataFrame."""
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data.index = pd.to_datetime(data.index)
        self.calc_returns(data)
        return data

    def calc_returns(self, data):
        """method that adds change and return columns to data"""
        data['Change'] = data['Close'].pct_change()  # change over time
        data['Return'] = data['Close'].pct_change().round(4)  # returns over time
        # tried using this code 'np.log([closing_price]).diff().round(4)' but was getting errors.

    def plot_return_dist(self):
        """method that plots instantaneous returns as histogram"""
        plt.hist(self.data['Return'], bins=50, color='r', edgecolor='w')
        plt.grid(axis='y', alpha=0.3)
        plt.xlabel('Return')
        plt.ylabel('Frequency')
        plt.title('Histogram of Instantaneous Returns')
        plt.show()

    def plot_performance(self):
        """method that plots stock object performance as percent."""
        plt.plot(self.data['Close'] / self.data['Close'].iloc[0] * 100, color='r')
        plt.grid(True)
        plt.xlabel('Date')
        plt.ylabel('Performance (%)')
        plt.title('Stock Performance Over Time')
        plt.show()


def main():  # had a lot of trouble with this one, couldnt figure out what was wrong
    my_stock = Stock("GOOG")
    print(my_stock.data)
    test.plot_performance()
    test.plot_return_dist()


if __name__ == '__main__':
    my_stock = Stock("GOOG")
    print(my_stock.data)
    my_stock.plot_return_dist()
    my_stock.plot_performance()
