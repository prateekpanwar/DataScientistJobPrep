# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:19:54 2019

@author: Visitor
"""

from sklearn.datasets import load_boston
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

boston = load_boston()
data = pd.DataFrame(boston.data)
data.columns = boston.feature_names
data['PRICE'] = boston.target

#print(data.info())
#print(data.describe) #gives you mean, std etc for each col

#XGBoost doesnt work on categorical features so apply some encoding 
#XGBoost also can handle missing values (NaN) by itself so upto you to change them or leave them
#Default base learners for XGBoost are Trees

X, y = data.iloc[:,:-1], data.iloc[:,-1]

data_dmatrix = xgb.DMatrix(data=X, label=y) #optimizing the performance of XGBoost

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

xg_reg = xgb.XGBRegressor(objective='reg:linear', colsample_bytree=0.3, learning_rate= 0.1,
                          max_depth = 5, alpha=10, n_estimators=10)

xg_reg.fit(X_train,y_train)

preds = xg_reg.predict(X_test)

#########################Computing the performance###########################

rmse = np.sqrt(mean_squared_error(y_test, preds))

print('RMSE: ', rmse)

########################k-cross validation###################################

params = {"objective":"reg:linear",'colsample_bytree': 0.3,'learning_rate': 0.1,
                'max_depth': 5, 'alpha': 10}

cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3,
                    num_boost_round=50, early_stopping_rounds=10, metrics='rmse',
                    as_pandas=True, seed=123)     #early_stopping_rounds finishes trainning if the results doesnt improve for that round

##############visualizing the boost###########################################

xg_reg = xgb.train(params=params, dtrain=data_dmatrix, num_boost_round=10)

#xgb.plot_tree(xg_reg, num_trees=0)
#plt.rcParams['figure:figsize'] = [50, 10]
#plt.show()

###############importance of each features#################
xgb.plot_importance(xg_reg)
plt.rcParams['figure.figsize'] = [5, 5]
plt.show()