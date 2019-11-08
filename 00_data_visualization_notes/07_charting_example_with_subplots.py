import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import style
from pandas_datareader import data
import pandas as pd


def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas


style.use('fivethirtyeight')

start_date = '2019-05-01'
end_date = '2019-11-01'

df = data.DataReader('AAPL', 'yahoo', start_date, end_date)

# ensuring only equity series is considered
df['Date'] = df.index

# Converting date to pandas datetime format
df['Date'] = pd.to_datetime(df['Date'])
df["Date"] = df["Date"].apply(mdates.date2num)

# Creating required data in new DataFrame OHLC
ohlc = df[['Date', 'Open', 'High', 'Low', 'Close']].copy()

fig = plt.figure()

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
# You cannot write ax2.ylabel, so you have to leave this JUST BELOW the axis you defined
plt.ylabel('Price')
ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

# Plot the high_minus_low volatility indicator


def high_minus_low(high, low):
    return high - low


highs = np.array(df['High'])
lows = np.array(df['Low'])
hml = list(map(high_minus_low, highs, lows))
date = np.array(df['Date'])

ax1.plot(date, hml)

# plot the candlesticks
candlestick_ohlc(ax2, ohlc.values, width=.4,
                 colorup='#77d879', colordown='#db3f3f')
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# 6 values in the x axis
ax2.xaxis.set_major_locator(mticker.MaxNLocator(6))

bbox_props = dict(
    boxstyle='larrow, pad=0.3',
    fc='#f2f1f1',  # font color
    ec='k',         # edge color
    lw=2           # line width
)
ax2.annotate(
    str(ohlc['Close'][-1]),
    (ohlc['Date'][-1], ohlc['Close'][-1]),
    xytext=(ohlc['Date'][-1] + 3, ohlc['Close'][-1]),
    bbox=bbox_props
)

# moving averages
MA1 = 10
MA2 = 30
ma1 = moving_average(np.array(df['Close']), MA1)
ma2 = moving_average(np.array(df['Close']), MA2)

date = np.array(df['Date'])
start = len(date[MA2-1:])
# dimensions have to match
ax3.plot(date[-start:], ma1[-start:])
ax3.plot(date[-start:], ma2[-start:])

# xytext: we can move the position of the annotation elsewhere too
# 0.8, 0.9: in percents w.r.t. the axes, see "axes fraction"
plt.subplots_adjust(left=.11, bottom=.16, right=.9,
                    top=.95, wspace=.2, hspace=.2)

# Saving image
#plt.savefig('OHLC HDFC.png')

# In case you dont want to save image but just displya it
plt.show()
