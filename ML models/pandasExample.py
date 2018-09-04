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