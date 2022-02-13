# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
Simple program to sort the dict items
"""

# Wrong solution

d={'b':10,'a':1,'c':22}
t=d.items()
print (t)
print ("After sorting the elements:")
# t.sort(reverse=True)
# print (t)

for key,value in d.items():
    print (value,key)
    