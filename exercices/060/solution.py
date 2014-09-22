# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 19:03:10 2014

@author: ne
"""

ab = "abcdefghijklnmopqrstuvwxyz"

for i in range(len(ab)):
    for j in range(len(ab)):
        print(ab[i] + ab[j])