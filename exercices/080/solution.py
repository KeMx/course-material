# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 19:08:15 2014

@author: ne
"""

ab = "abcdefghijklmnopqrstuvwxyz"
for i in ab:
    for j in ab:
        if i < j:
            print(i + j)
