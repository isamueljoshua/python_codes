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
    
# [(3, 'but'), (4, 'soft'), (4, 'what'), (5, 'light'), (2, 'in'), (6, 'yonder'), (6, 'window'), (6, 'breaks')]
print(t)
t.sort(reverse=True)
# After Sorting: [(6, 'yonder'), (6, 'window'), (6, 'breaks'), (5, 'light'), (4, 'what'), (4, 'soft'), (3, 'but'), (2, 'in')]
print("After Sorting:",t)
res = list()
for length, word in t:
    res.append(word)
# ['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']
print(res)