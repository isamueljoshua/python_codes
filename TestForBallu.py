# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 14:44:41 2017

@author: Administrator
"""

lst=[1,2,3]
res=1.0
for i in range(len(lst)):
    for j in range(len(lst)):
        if i!=j:
            print "Before:",res
            print "lst[i]=",lst[i]
            print "lst[j]=",lst[j]
            var=lst[j]-lst[i]
            print "var=",var
            res=res*(float(lst[i])/float(var))
            print "After:",res