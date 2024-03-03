# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
Created on Fri Sep 22 12:36:34 2017
"""

fname = input('Enter the file name:')
try:
    fhand=open(fname)
except:
    print("File cannot be opened")
    exit()

counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

print (counts)

for line in fhand:
    words=line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
        
print ("\nUsing the get method now",counts)