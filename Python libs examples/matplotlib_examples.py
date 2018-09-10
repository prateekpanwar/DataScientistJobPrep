# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 19:46:54 2018

@author: hp1
"""

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

import seaborn as sb

rcParams['figure.figsize'] = 5, 4
sb.set_style('whitegrid')

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]


plt.plot(x, y)

########using Pandas data frames###################################
address = './mtcars.csv'
cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
mpg = cars['mpg']

mpg.plot() #From pandas

df = cars[['cyl', 'wt', 'mpg']]
df.plot() #from pandas

plt.figure(1)
plt.bar(x,y)

mpg.plot(kind='bar')

mpg.plot(kind='barh') #for horizontal

plt.figure(2)
plt.pie(y) 
plt.show()

plt.savefig('pie_chart.jpg') #Saving the pie chart
plt.show()

########################object orientented plots######################
fig = plt.figure()

ax = fig.add_axes([.1, .1, 1, 1])

ax.plot(x,y)

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])

ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.set_xticks([0,1,2,4,5,6,7,8,9,10])
ax.set_yticks([0,1,2,3,4,5])

ax.grid()

ax.plot(x,y)
##########################Subplot######################################
fig = plt.figure()

fig, (ax1, ax2) = plt.subplot(1,2)

ax1.plot(x)
ax2.plot(y)