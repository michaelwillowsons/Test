# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:14:28 2024

@author: willom
"""
# added user input 
def multi(c=0,d=0, user = False):
    if user:
        c = int(input("c = "))
        d = int(input("d = "))
    ans = c*d
    return ans

print(multi(4,6))

print(multi(user = True))


