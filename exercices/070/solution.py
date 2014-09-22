# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 19:06:16 2014

@author: ne
"""

ab = "abcdefghijklnmopqrstuvwxyz"

for i in range(len(ab)):
    for j in range(len(ab)):
       if i != j:
           print(ab[i] + ab[j])