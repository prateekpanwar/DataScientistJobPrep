# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:51:33 2018

@author: hp1
"""

def printingNums(num):
    if num>=0:
        printingNums(num-1)
        print(num)

printingNums(10)