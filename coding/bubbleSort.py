# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 18:07:59 2018

@author: hp1
"""

def bubbleSort(sortList):
    for i in range(len(sortList)-1):
        for j in range(len(sortList)-i-1):
            temp = 0
            if sortList[j]>sortList[j+1]:
                temp = sortList[j+1]
                sortList[j+1] = sortList[j]
                sortList[j] = temp
    return sortList
                
                


print(bubbleSort([5,8,6,1,2,8,9,6,4,100,0]))