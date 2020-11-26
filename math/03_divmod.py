# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
Problem source: https://www.hackerrank.com/challenges/python-mod-divmod/problem
One of the built-in functions of Python is divmod, 
which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder a.

Input:
177
10

Output:
17
7
(17, 7)
"""
a, b = int(input()), int(input())
div = divmod(a, b)

print(div[0])
print(div[1])
print(div)