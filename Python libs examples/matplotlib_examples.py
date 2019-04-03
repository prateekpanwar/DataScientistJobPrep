# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 19:46:54 2018

@author: hp1
"""

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame
from pandas.plotting import scatter_matrix

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

fig, (ax1, ax2) = plt.subplots(1,2)

ax1.plot(x)
ax2.plot(y)
########################Customize the graphs###########################

x = range(1, 10)
y = [1,2,3,4,0.5,4,3,2,1]

plt.figure()
plt.bar(x, y)

plt.figure()
wide = [0.5, 0.5, 0.5, 0.9, 0.9, 0.9, 0.5, 0.5, 0.5]
color = ['salmon']
(plt.bar(x,y, width=wide, color=color, align='center'))

cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = cars[['cyl', 'mpg','wt']]
plt.figure()
df.plot()

plt.figure()
color_theme = ['darkgray', 'lightsalmon', 'powderblue']
df.plot(color=color_theme)

z = [1,2,3,4,0.5]
plt.figure()
plt.pie(z)
plt.show()

color_theme = ['#A9A9A9', '#FFA07A', '#B0E0E6', '#FFE4C4', '#BDB76B']
plt.figure()
plt.pie(z, colors = color_theme)
plt.show()

x1 = range(0,10)
y1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.plot(x, y)
plt.plot(x1,y1)

plt.figure()
plt.plot(x,y, ls = 'steps', lw=5)
plt.plot(x1,y1, ls = '--', lw = 10)

plt.figure()
plt.plot(x,y, marker='1', mew=15)
plt.plot(x1, y1, marker='*', mew=20)

####################label and annotations##########################################

x = range(1,10)
y = [1,2,3,4,0.5,4,3,2,1]
plt.figure()
plt.bar(x,y)

plt.xlabel('your x-axis label')
plt.ylabel('your y-axis label')

z = [1 , 2, 3, 4, 0.5]
veh_type = ['bicycle', 'motorbike','car', 'van', 'stroller']
plt.figure()
plt.pie(z, labels= veh_type)
plt.show()

cars = pd.read_csv(address)
cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

mpg = cars.mpg #Another way to select a col

fig = plt.figure()
ax = fig.add_axes([.1, .1, 1, 1])

mpg.plot()

ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names, rotation=60, fontsize=('medium'))

ax.set_title('Miles per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

plt.figure()
plt.pie(z)
plt.legend(veh_type, loc='best')
plt.show()

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names, rotation=60, fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

ax.legend(loc='best')

print(mpg.max())

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
mpg.plot()
ax.set_title('Miles per Gallon of Cars in mtcars')
ax.set_ylabel('miles/gal')

ax.set_ylim([0,45])

ax.annotate('Toyota Corolla', xy=(19,33.9), xytext = (21,35),
           arrowprops=dict(facecolor='black', shrink=0.05))


##################################hist#####################################

mpg = cars.mpg
plt.figure()
mpg.plot(kind='hist')

plt.figure() #different way
plt.hist(mpg)
plt.plot()

plt.figure() #with seaborn
sb.distplot(mpg)

#################################scatter##################################
plt.figure()
cars.plot(kind='scatter', x='hp', y='mpg', c=['darkgray'], s=150)

plt.figure()
sb.regplot(x='hp', y='mpg', data=cars, scatter=True)

#plt.figure()
#sb.pairplot(cars)

#cars_df = pd.DataFrame((cars.iloc[:,1:6].values), columns = ['mpg', 'disp', 'hp', 'wt'])
#plt.figure()
#cars_target = cars.iloc[:,9].values
#target_names = [0, 1]
#
#cars_df['group'] = pd.Series(cars_target, dtype='category')
#sb.pairplot(cars_df, hue='group', palette='hls')

#########################box plot#########################################

plt.figure()
cars.boxplot(column='mpg', by='am')
plt.figure()
cars.boxplot(column='wt', by='am')

cars.boxplot(column='mpg', by='am')
sb.boxplot(x='am', y='mpg', data=cars, palette='hls')
