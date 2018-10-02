# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 01:15:39 2018

@author: hp1
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA, TruncatedSVD

from sklearn.datasets import load_boston

boston = load_boston()

df_x = pd.DataFrame(boston.data, columns=boston.feature_names)
print(df_x.head())
df_y = pd.DataFrame(boston.target)

reg = linear_model.LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
reg.fit(x_train, y_train)

print(reg.score(x_test, y_test))

pca = PCA(n_components=10, whiten='True') #reduction to 10 dimensions
x = pca.fit(df_x).transform(df_x)

print(pca.explained_variance_) # only 3% reduction when reducing from 18 features to 10 

####now testing the model again on the reduced dimensions
reg = linear_model.LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(x, df_y, test_size=0.2, random_state=4)
reg.fit(x_train, y_train)

print(reg.score(x_test, y_test)) #accuracy decreased 
