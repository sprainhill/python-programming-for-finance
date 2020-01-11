import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

## data frame
df = web.DataReader('TSLA', 'yahoo', start, end)

# print(df.head(10))
# print(df.tail(10))

## generate a csv file
# df.to_csv('tsla.csv')

## read in a csv
df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

print(df.head(10))
print(df['Adj Close'])
print(df[['Open', 'High']])

df['Adj Close'].plot()
plt.show()