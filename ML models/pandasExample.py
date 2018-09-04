# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 20:55:19 2018

@author: hp1
"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'])

series_obj['row 7'] # to get the value at that index

