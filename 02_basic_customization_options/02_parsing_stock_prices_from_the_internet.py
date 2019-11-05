import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib.request
import numpy as np


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.datestr2num(fmt)

    def bytes_converter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytes_converter


def graph_data(stock):
    print('Currently pulling: ', stock)
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + \
        stock + '&interval=5min&apikey=K6QCETUG7BJZW11N&datatype=csv'
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for each_line in split_source:
        split_line = each_line.split(',')
        if len(split_line) == 6:
            if 'values' not in each_line:
                stock_data.append(each_line)

    for d in stock_data:
        print(d)


stock = input('Stock to plot: ')
graph_data(stock)
