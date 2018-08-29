# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:11:57 2018

@author: hp1
"""

def get_fib(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    elif(position>=2):
        return (get_fib(position-1) + get_fib(position-2))


for i in range(9):
    print (get_fib(i))


