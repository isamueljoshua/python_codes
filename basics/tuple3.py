# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:49:45 2017

@author: Administrator
"""

m=['have','fun']
#Making a tuple from the value in the list
(x,y) = m
print( "x=",x)
print("y=",y)

addr="monty@python.org"
uname,domain = addr.split("@")
print(uname)
print(domain)