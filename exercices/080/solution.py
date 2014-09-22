# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 19:08:15 2014

@author: ne
"""


ab = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(ab)):
    for j in range(len(ab)):
        if i < j:
            print(ab[i] + ab[j])
