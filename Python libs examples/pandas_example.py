# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:55:19 2018

@author: hp1
"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

###################################creating a series####################################
series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'])

print(series_obj['row 7']) # to get the value at that index

print(series_obj[[5,6]]) #to get the index

print(series_obj[series_obj > 6])

series_obj['row 1', 'row 2', 'row 5'] = 8

print(series_obj)
##################################Creating a data frame##################################

np.random.seed(25) #printing exact random numbers

DF_obj = DataFrame(np.random.rand(36).reshape(6,6), index= ['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
                   columns = ['col 1', 'col 2', 'col 3', 'col 4', 'col 5', 'col 6'])

print(DF_obj)

print(DF_obj.loc[['row 1', 'row 5'], ['col 3', 'col 4']])

print(DF_obj['row 1': 'row 5'])

print(DF_obj < .2) #Comparision

###################################Replacing missing values#############################

missing  = np.nan

series_obj = Series(['row 1', missing, 'row 3', 'row 4', 'row 5', missing, 'row 7', 'row 8'])

print (series_obj)

print(series_obj.isnull())

np.random.seed(25)

DF_obj = DataFrame(np.random.rand(36).reshape(6,6))

DF_obj.loc[3:5, 0] = missing
DF_obj.loc[1:4, 5] = missing

print(DF_obj)

fill_DF = DF_obj.fillna(0)

print(fill_DF)

fill_DF = DF_obj.fillna({0: 0.1, 5:1.25}) #Replacing with Dict

print(fill_DF)

fill_DF = DF_obj.fillna(method='ffill') #replace by the last know value in that col

print(fill_DF)

print(DF_obj.isna().sum()) #counting nan for each row

fill_DF = DF_obj.dropna() #Dropping all the rows with nan

print(fill_DF)

fill_DF = DF_obj.dropna(how='all') #Drop only those rows which has all the values nan

print(fill_DF)

############################Removing dulplicates#####################################

missing  = np.nan

series_obj = Series(['row 1', missing, 'row 3', 'row 4', 'row 5', missing, 'row 7', 'row 8'])

print (series_obj)

DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                  'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                  'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})

print(DF_obj)
print(DF_obj.duplicated()) #Check duplicates

print(DF_obj.drop_duplicates())

DF_obj = DataFrame({'column 1': [1, 1, 2, 2, 3, 3, 3],
                  'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                  'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})

print(DF_obj)

print(DF_obj.drop_duplicates(['column 3'])) #look for dupicates in col 3 and drop those rows


####################################Concatenate###########################################

DF_obj = DataFrame(np.arange(36).reshape(6,6))

print(DF_obj)

DF_obj_2 = DataFrame(np.arange(15).reshape(5,3))

print(DF_obj_2)

print(pd.concat([DF_obj, DF_obj_2], axis = 1)) #axis 1 means along the col

print(pd.concat([DF_obj, DF_obj_2])) #Along the rows

print(DF_obj.drop([0,2])) #Dropping particular rows

print(DF_obj.drop([1,4], axis=1))

series_obj = Series(np.arange(6))

series_obj.name = "testing"

print(series_obj)

variable_added = DataFrame.join(DF_obj, series_obj) #For adding in col

print(variable_added)

added_variable = variable_added.append(variable_added, ignore_index=False) #adding in the rows. Index=True re-index all the table

print(added_variable)

DF_sorted = DF_obj.sort_values(by=[5], ascending=False) #sort by col 5

print(DF_sorted)

###############using the data file to group#####################################

address = './mtcars.csv'

cars = pd.read_csv(address)

cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

print(cars.head())

cars_groups = cars.groupby(cars['cyl'])

cars_groups.mean()
print(cars_groups)

############################Extras#######################################
df = df['col1'].apply(pd.Series) #Expanding columns
