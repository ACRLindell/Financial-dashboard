

import numpy as np
import pandas as pd 
from datascroller import scroll
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime as dt
 
class Analysis(object):
    def __init__(self, ticker,timeframe):
        self.ticker = ticker
        self.timeframe = timeframe
    def read_from_csv(ticker,):
        
""" def analysis(ticker):
    print(ticker)
    path ='../Stockdata/Stocks/' + ticker
    print(path)
    data = pd.read_csv('./Stockdata/Stocks/'+ticker+'.csv')
    print(data.var()

analysis("ABB.ST")     """

df = pd.read_csv('./Stock dashboard/Stocks/CAST.ST.csv',index_col=0,parse_dates=True)

#mpf.plot(df, type="candle")
#print(df['2020-12-01':'2020-12-02'])

#RSI 
delta = df['Adj Close'].diff().dropna()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13,adjust=False).mean()
ema_down = down.ewm(com=13,adjust=False).mean()
rs = abs(ema_up/ema_down)
df['RSI'] = 100 - (100/(1+rs))
df['RSI'] = df['RSI'].iloc[14:]
#print(df['RSI'].iloc[0:50])
#plt.plot(df['RSI'])
#plt.show()

#Stochastic RSI
min_value = df['RSI'].rolling(window=14,center=False).min()
max_value = df['RSI'].rolling(window=14,center=False).max()
stochRSI =((df['RSI']-min_value)/(max_value-min_value))*100
df['Fast Stochastic'] = K = stochRSI.rolling(window=3,center=False).mean()
df['Slow Stochastic'] = K.rolling(window=3,center=False).mean()
#print(K)
#print(D)
#print(df)

#SMA
df['SMA20']=sma_20 = df['Adj Close'].rolling(window=20).mean()
df['SMA50']=sma_50 = df['Adj Close'].rolling(window=50).mean()
df['SMA100']=sma_100 = df['Adj Close'].rolling(window=100).mean()
df['SMA200']=sma_200 = df['Adj Close'].rolling(window=200).mean()
#print(df.iloc[0:50])
""" plt.plot(df['Adj Close'])
plt.plot(sma_20)
plt.plot(sma_50)
plt.plot(sma_100)
plt.plot(sma_200)
plt.show() """

#EMA
df['EMA20'] = ema_20 = df['Adj Close'].ewm(span=20,adjust=False).mean()
df['EMA50'] = ema_50 = df['Adj Close'].ewm(span=50,adjust=False).mean()
df['EMA100'] = ema_100 = df['Adj Close'].ewm(span=100,adjust=False).mean()
df['EMA200'] = ema_200 = df['Adj Close'].ewm(span=200,adjust=False).mean()

#Volatility 
df['Daily returns'] = np.log(df['Close']/df['Close'].shift(-1))
df['Daily std'] = np.std(df['Daily returns'])
std = df['Daily std']*252**0.5
#print(std)
#print(df)

#Bollinger bands 

rstd = df['Adj Close'].rolling(window=20).std()
df['BollingerUpper'] = sma_20 + 2 * rstd
df['BollingerLower'] = sma_20 - 2 * rstd
#plt.plot(df['BollingerLower'])
#plt.show()

#Backtesting 
mod = df.reset_index()
#mod['Date'] = mod['Date'].date()
#print(mod['Date'].date())
mod['Date'] = pd.to_datetime(mod['Date'])
mod['Date'] = mod['Date'].dt.date
mod = mod.dropna()
#scroll(mod)
#scroll(df)

#print(mod['Date'].iloc[1].strftime("%Y-%m-%d"))
buy = []
sell = []
state = 'Buy'
for n in range(0,len(mod)):
    #Buy state
    if state == 'Buy': 
        if mod['RSI'].iloc[n]<=25 and mod['Adj Close'].iloc[n] > mod['SMA200'].iloc[n] :
            buy.append([mod['Date'].iloc[n].strftime("%Y-%m-%d"),mod['Adj Close'].iloc[n]])
            state = 'Sell'
    else: 
    #Sell state
        if mod['RSI'].iloc[n]> 50 or mod['Adj Close'].iloc[n]< mod['SMA200'].iloc[n]:
            sell.append([mod['Date'].iloc[n].strftime("%Y-%m-%d"),mod['Adj Close'].iloc[n]])
            state = 'Buy'
print("Buy dates:") 
for num in range(0,len(buy)): 
    print(buy[num])
#print(buy)
print("Sell dates:")
for num2 in range(0,len(sell)): 
    print(sell[num2])
trades = []
for num in range(0,len(buy)): 
    trades.append((sell[num][1]-buy[num][1])/buy[num][1])
print("Trades:")  
for num3 in range(0,len(trades)):
    print(trades[num3]) 
