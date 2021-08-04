#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:46:53 2021

@author: apple
"""

import numpy as np
import pandas_datareader.data as pdr
import datetime
import pandas as pd
from pandas import DataFrame

from datetime import date
import yfinance as yf

#ind_nifty200list
#ind_niftysmallcap100list
#ind_nifty200list
#smallcap250
#next50
start = datetime.datetime.today()-datetime.timedelta(365)
end = datetime.datetime.today()
NSE_200 = pd.read_csv('/Users/apple/Downloads/ind_niftymidsmallcap400list2.csv')
print(NSE_200)
df = DataFrame(NSE_200)
Stock_LIST_DIC= {}
a_list = []


for x in df['Symbol']:
  try:
      x = x + '.NS'
      df = yf.download(x,start,end,interval='1D')
      DMA_200 = df['Close'].rolling(window=200).mean()
      DMA_50 = df['Close'].rolling(window=50).mean()[-1]
      Close_price = df['Close'][-1]
      roc = (df['Close'][-1] - df['Close'][0])/df['Close'][0]
      roc = roc *100
      Stock_LIST_DIC['name']= x 
      Stock_LIST_DIC['ROC'] = roc
      Stock_LIST_DIC['52weeklow'] = min(df["Close"][-260:])
      Stock_LIST_DIC['52weekHigh'] = max(df["Close"][-260:])
      Stock_LIST_DIC['Close_price'] =  Close_price
      Stock_LIST_DIC = Stock_LIST_DIC.copy()
      a_list.append(Stock_LIST_DIC)
      print(Stock_LIST_DIC)

      
  except:
      print("An exception occurred")

  
  
  
print(a_list) 
finaldata = pd.DataFrame(a_list)
finaldata_200 = finaldata.loc[(finaldata['Close_price']>=finaldata['DMA_200'])]

final_data_roc = finaldata.sort_values("ROC", axis = 0, ascending = False, 
                 inplace = True, na_position ='first')

