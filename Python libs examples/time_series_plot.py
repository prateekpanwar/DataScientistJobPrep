# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:37:14 2018

@author: hp1
"""

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')
 
address = './Superstore-Sales.csv'

df = pd.read_csv(address, index_col='Order Date', parse_dates=True,  encoding = "ISO-8859-1")

print(df.head())

plt.figure()
df['Order Quantity'].plot()

df2 = df.sample(n=100, random_state=25, axis=0)

plt.figure()
plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

df2['Order Quantity'].plot()