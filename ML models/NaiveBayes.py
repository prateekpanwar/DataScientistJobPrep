# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:28:45 2018

@author: hp1
"""

import numpy as np
import pandas as pd

import urllib

import sklearn
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split

dataset = pd.read_csv('spambase.data')


#dataset = np.loadtxt(raw_data, delimiter=",")

X = dataset.iloc[:, 0:dataset.columns.size-1]
y = dataset.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.33, random_state=17)

BernNB = BernoulliNB(binarize=True)
BernNB.fit(X_train, y_train)
print(BernNB)

y_expect = y_test
y_pred = BernNB.predict(X_test)
print (accuracy_score(y_expect, y_pred))

MultiNB = MultinomialNB()

MultiNB.fit(X_train, y_train)
print(MultiNB)

y_pred = MultiNB.predict(X_test)
print (accuracy_score(y_expect, y_pred))

GausNB = GaussianNB()
GausNB.fit(X_train, y_train)
print(GausNB)

y_pred = GausNB.predict(X_test)
print (accuracy_score(y_expect, y_pred))

####################trying to improve the accuracy/try and error##########################
BernNB = BernoulliNB(binarize=0.1)
BernNB.fit(X_train, y_train)
print(BernNB)

y_expect = y_test
y_pred = BernNB.predict(X_test)
print (accuracy_score(y_expect, y_pred))