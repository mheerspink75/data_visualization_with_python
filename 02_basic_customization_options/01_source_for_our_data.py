import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib.request
import numpy as np 

# https://cloud.iexapis.com/stable/stock/aapl/chart/5y?token=pk_553865f4628a441bbe94785fe772e5d5

def graph_data(stock):
    print('Currently pulling: ', stock)
    url = 'https://cloud.iexapis.com/stable/stock/' + stock + '/chart/5y?token=pk_553865f4628a441bbe94785fe772e5d5&format=csv'
    source_code = urllib.request.urlopen(url).read().decode()
    print(source_code)

stock = input('Stock to plot: ')
graph_data(stock)
