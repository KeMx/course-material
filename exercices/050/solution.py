# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:58:31 2014

@author: ne
"""
sum = 0
for i in range(1001):
    if i%3:
        sum = sum + i
        
    elif i%5:
        sum = sum + i

print(sum)