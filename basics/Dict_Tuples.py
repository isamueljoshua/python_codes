# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
Simple program to sort the dict items
"""

d={'b':10,'a':1,'c':22}
t=d.items()
print (t)
print ("After sorting the elements:")

# Sort by keys
op = sorted(t)
print (op)

# Sort by values
srt_values = {k: v for k, v in sorted(t, key=lambda item: item[1])}
print("Sort by values: ", srt_values)

for key,value in d.items():
    print (key,value)
    