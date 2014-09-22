# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 19:06:16 2014

@author: ne
"""

ab = "abcdefghijklmnopqrstuvwxyz"

for i in ab:
    for j in ab:
        if i != j:
            print(i + j)
