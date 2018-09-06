# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 21:04:59 2018

@author: hp1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as mat
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams

import sklearn
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets

rcParams['figure.figsize'] = 5,4
sb.set_style('whitegrid')

iris = datasets.load_iris()

x = iris.data

variable_name = iris.feature_names

print(x[1:10])

pca = decomposition.PCA()

iris_pca = pca.fit_transform(x)

print(pca.explained_variance_ratio_) #how much information is compressed in the first few components
print(pca.explained_variance_ratio_.sum()) #Cumulative variance. 1 tells you that 100% info was captured but we dont want 100%. Always keep 70% of the data info

comps = pd.DataFrame(pca.components_, columns=variable_name)

print(comps)

sb.heatmap(comps)
