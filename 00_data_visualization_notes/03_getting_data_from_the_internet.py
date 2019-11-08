from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

start_date = '2012-01-01'
end_date = '2019-11-01'

panel_data = data.DataReader('AAPL', 'yahoo', start_date, end_date)
print(panel_data.head(9))

panel_data2 = data.DataReader(['AAPL', 'MSFT', '^GSPC'], 'yahoo', start_date, end_date)
panel_data2['Close'][['AAPL', 'MSFT']].plot()

panel_data3 = data.DataReader(['AAPL'], 'yahoo', start_date, end_date)
panel_data3['Close'][['AAPL']].plot()

x = np.array(panel_data3.index)
y = np.array(panel_data3['Close']['AAPL'])
plt.fill_between(x, y, 0, alpha=0.3)
plt.grid(True, color='g', linestyle='dotted')
plt.show()

x = np.array(panel_data3.index)
y = np.array(panel_data3['Close']['AAPL'])
plt.fill_between(x, y, 125, alpha=0.5, where=(y >= 125), facecolor='g')
plt.fill_between(x, y, 125, alpha=0.5, where=(y < 125), facecolor='r')
plt.show()

