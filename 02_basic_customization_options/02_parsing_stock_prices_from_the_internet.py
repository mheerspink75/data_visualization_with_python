import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib.request
import numpy as np 

# https://cloud.iexapis.com/stable/stock/aapl/chart/5y?token=pk_553865f4628a441bbe94785fe772e5d5

def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.datestr2num(fmt)
    def bytes_converter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytes_converter

def graph_data(stock):
    print('Currently pulling: ', stock)
    url = 'https://cloud.iexapis.com/stable/stock/' + stock + '/chart/1y?token=pk_553865f4628a441bbe94785fe772e5d5&format=csv'
    source_code = urllib.request.urlopen(url).read().decode()
#    stock_data = []
 #   split_source = source_code.split('\n')

  #  for each_line in split_source:
   #     split_line = each_line.split(',')
    #    if len(split_line) == 6:
     #       if 'values' not in each_line:
      #          stock_data.append(each_line)

    date, close, high, low, open, volume = np.loadtxt(source_code, delimiter = ',', unpack=True, converters={0: bytespdate2num('%Y-%m-%d')})

    print(date)

stock = input('Stock to plot: ')
graph_data(stock)