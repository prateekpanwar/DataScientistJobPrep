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
import matplotlib.pyplot as plt

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

##########################################using different dataset##############################

data = pd.read_csv('mnist.csv') #mnists handwritten digits dataset
print(data.head())

df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

rf = RandomForestClassifier(n_estimators=50)
rf.fit(x_train, y_train)

pred = rf.predict(x_test)

score = y_test.values

count = 0
for i in range(len(pred)):
    if pred[i] ==score[i]:
        count = count+1
print(count/float(len(pred)))

##############using PCA############

pca = PCA(n_components=25, whiten='True') #reduction to 10 dimensions
x = pca.fit(df_x).transform(df_x)

x_train, x_test, y_train, y_test = train_test_split(x, df_y, test_size=0.2, random_state=4)

rf = RandomForestClassifier(n_estimators=50)
rf.fit(x_train, y_train)

pred = rf.predict(x_test)

score = y_test.values

count = 0
for i in range(len(pred)):
    if pred[i] ==score[i]:
        count = count+1
print(count/float(len(pred))) # from 800 to 25 features, the accuracy only dropped 2%

print(pca.explained_variance_) #gives variance of each feature in decending order... tells you how much orginal information in each new feature

########################visualizing the PCA features###########################

pca = PCA(n_components=2, whiten='True') #reduction to 10 dimensions
x = pca.fit(df_x).transform(df_x)

x_train, x_test, y_train, y_test = train_test_split(x, df_y, test_size=0.2, random_state=4)

rf = RandomForestClassifier(n_estimators=50)
rf.fit(x_train, y_train)

pred = rf.predict(x_test)

score = y_test.values

count = 0
for i in range(len(pred)):
    if pred[i] ==score[i]:
        count = count+1
print(count/float(len(pred)))

y = df_y.values

for i in range(5000): #ploting only 5000 samples
    if y[i] == 0: # separating 0 from the dataset
        plt.scatter(x[i,1], x[i,0], c='r')
    else:
        plt.scatter(x[i,1], x[i,0], c='g')
plt.show()