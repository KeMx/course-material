# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 19:13:15 2014

@author: ne
"""


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
