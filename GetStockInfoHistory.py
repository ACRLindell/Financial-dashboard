import numpy as np
import pandas as pd 
from pandas_datareader import data as web
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import datetime as dt
import mplfinance as mpf

def save_to_csv_from_yahoo(ticker,syear,smonth,sday,eyear,emonth,eday):
    start = dt.datetime(syear,smonth,sday)
    end = dt.datetime(eyear,emonth,eday)

    df = web.DataReader(ticker,'yahoo',start,end)
    df.to_csv("/Users/alexanderlindell/Documents/Programmering /Python/Stock dashboard/Stocks/" + ticker + '.csv')
    return df
tickers =pd.read_csv("/Users/alexanderlindell/Documents/Programmering /Python/Stock dashboard/Tickers.csv")
#print(tickers['Ticker'][1])
for tic in tickers['Ticker']:
    try:
        save_to_csv_from_yahoo(tic,2000,1,1,2022,3,6)
    except IOError:
        print("Could not find stock:" + tic )
            
#save_to_csv_from_yahoo(tickers['Ticker'][0],2000,1,1,2022,1,1)

#save_to_csv_from_yahoo('CAST.ST',2000,1,1,2021,3,3)



