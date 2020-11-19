# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 21:43:07 2017

@author: Administrator
"""

txt = 'but soft what light in yonder window breaks'
words = txt.split()

t = list()
for word in words:
    t.append((len(word), word))
    
print t
t.sort(reverse=True)
print "After Sorting:",t
res = list()
for length, word in t:
    res.append(word)
print res