import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc

from pandas_datareader import data
import pandas as pd

start_date = '2019-10-01'
end_date = '2019-11-01'

df = data.DataReader('AAPL', 'yahoo', start_date, end_date)

# ensuring only equity series is considered
df['Date'] = df.index

# Converting date to pandas datetime format
df['Date'] = pd.to_datetime(df['Date'])
df["Date"] = df["Date"].apply(mdates.date2num)

# Creating required data in new DataFrame OHLC
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']].copy()
# In case you want to check for shorter timespan
# ohlc =ohlc.tail(60)

f1, ax = plt.subplots(figsize=(10, 5))

# plot the candlesticks
candlestick_ohlc(ax, ohlc.values, width=.4,
                 colorup='#77d879', colordown='#db3f3f')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# 6 values in the x axis
ax.xaxis.set_major_locator(mticker.MaxNLocator(6))

ax.annotate(
    'Apple News',
    (ohlc['Date'][6], ohlc['Close'][6]),
    xytext=(0.2, 0.6),
    textcoords='axes fraction',
    arrowprops=dict(facecolor='#5a5a5a', color='#5a5a5a')
)
# xytext: we can move the position of the annotation elsewhere too
# 0.8, 0.9: in percents w.r.t. the axes, see "axes fraction"

# Saving image
#plt.savefig('OHLC HDFC.png')

# In case you dont want to save image but just displya it
plt.show()
