"""
dictionary1.py

Author: Samuel Joshua

Description:
    This script demonstrates two methods to count the number of occurrences of each letter in a given string (in this case, the name 'samuel joshua') using Python dictionaries.

Features:
    - Method 1: Uses a standard dictionary and checks if a character is already present before incrementing its count.
    - Method 2: Uses the dictionary's get() method to simplify the counting logic.
    - Demonstrates how to safely retrieve values from a dictionary using get(), with a default value if the key is not present.

Usage:
    Run the script to see the count of each character in the string and examples of using the get() method.
"""
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