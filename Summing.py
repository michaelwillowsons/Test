# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:07:19 2024

@author: willom
"""
# Function to add three numbers
# Better defaults
def add(a=0,b=0,c=0):
    ans = a+b+c
    return ans

print(add(3,4))

# test case
# 1+2+3=6
if add(1,2,3) == 6:
    print("Test passed")
else:
    print("Test failed")