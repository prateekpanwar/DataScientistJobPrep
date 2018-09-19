# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:51:31 2018

@author: hp1
"""

l = []

for i in range(1001):
    if i%13 == 0 or i%31 ==0:
        l.append(i)

print(sum(l))