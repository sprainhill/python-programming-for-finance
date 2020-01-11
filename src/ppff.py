Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

# # data frame
df = web.DataReader('TSLA', 'yahoo', start, end)

# print(df.head(10))
# print(df.tail(10))

## generate a csv file
df.to_csv('tsla.csv')

## read in a csv
## df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

# print(df.head(10))

df.plot()
plt.show()
