# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 21:30:54 2017

@author: Administrator
"""

tup=('a','b','c','d','e')
print(type(tup))
# ('a', 'b', 'c', 'd', 'e')
print (tup)

t=tuple('sammyJ')
# ('s', 'a', 'm', 'm', 'y', 'J')
print (t)
# s
print (t[0])
# ('a', 'm')
print (t[1:3])

# Replacing one tuple with another
t=('A',) + t[1:]
# ('A', 'a', 'm', 'm', 'y', 'J')
print (t)

t1=(0,1,2)
t2=(0,3,4)
# True
print (t1<t2)

t1=(0,1,20000)
t2=(0,3,4)
# True
print (t1<t2)
