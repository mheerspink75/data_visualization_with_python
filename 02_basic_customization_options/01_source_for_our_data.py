import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib.request
import numpy as np


def graph_data(stock):
    print('Currently pulling: ', stock)
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + \
        stock + '&interval=5min&apikey=K6QCETUG7BJZW11N&datatype=csv'
    source_code = urllib.request.urlopen(url).read().decode()
    print(source_code)


stock = input('Stock to plot: ')
graph_data(stock)
