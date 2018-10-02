# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 02:21:53 2018

@author: hp1
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

data = pd.read_csv('mnist.csv')

df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]

x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)

#############decision tree####################
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)

print(dt.score(x_test, y_test))

print(dt.score(x_train, y_train)) #accuracy is 1 model is overfitting

#############Random forest###################

rf = RandomForestClassifier(n_estimators=10)
rf.fit(x_train, y_train)

print(rf.score(x_test, y_test))

###################Bagging##################

bg = BaggingClassifier(DecisionTreeClassifier(), max_samples=0.5, max_features=1.0, n_estimators=20)
bg.fit(x_train, y_train)
print(bg.score(x_test, y_test))

###################boosting##################
adb = AdaBoostClassifier(DecisionTreeClassifier(), n_estimators=10, learning_rate=1) #always adjust the learning rate to avoid overfitting
adb.fit(x_train, y_train)
print(adb.score(x_test, y_test))

print(adb.score(x_train, y_train)) #overfitting!

###################Voting classifier Model ensemble################
lr = LogisticRegression()
svm = SVC(kernel='poly', degree=2)
dt = DecisionTreeClassifier()

evc = VotingClassifier(estimators=[('lr', lr),('dt', dt),('svm', svm)], voting = 'hard') #hard means the votes are on labels and not on the probabilities
evc.fit(x_train.iloc[1:4000], y_train[1:4000]) #reducing to save computation

print(evc.score(x_test, y_test))
