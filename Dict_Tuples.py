# -*- coding: utf-8 -*-
"""
Simple program to sort the dict items
"""

d={'a':10,'b':1,'c':22}
t=d.items()
print (t)
print ("After sorting the elements:")
# t.sort(reverse=True)
# print (t)

for key,value in d.items():
    print (value,key)
    