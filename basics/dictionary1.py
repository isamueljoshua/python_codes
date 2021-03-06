# coding: utf-8

__author__ = ["Samuel Joshua"]

# Program to count the number of occourences of a letter in python
word = 'samuel joshua'
# Method 1
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print("The number of occourences of a letter in my name")
print (d)

# Method 2
print ("Using the get method")
# get returns the value of the key a 
print (d.get('a',0))
print (d.get('y',0))
print ("Using the get method-creating a dictionary")
dt = dict()
for a in word:
    dt[a] = dt.get(a,0)+1
print (dt)