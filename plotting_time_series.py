import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates

plt.style.use("seaborn")
data = pd.read_csv('data_timeseries.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date =data['Date']
price_close = data['Close']
# Open = data['Open']
# High = data['High']
# Low = data['Low']
# AdjClose = data['Adj Close']
# Volume = data['Volume']
plt.plot_date(price_date, price_close, linestyle='solid', color='green')
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter("%b, %d %Y")
#plt.gca().xaixs.set_major_formatter(date_format)

plt.title("Bitcoin prices")
plt.tight_layout()
plt.xlabel("Date ")
plt.ylabel("Closing price")
#plt.legend()
plt.show()