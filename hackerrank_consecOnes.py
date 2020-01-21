# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:16:10 2017

@author: Administrator
"""

n=int(raw_input("Enter a number:").strip())
count = 0
max_one_count = 0
bin_conv = bin(n)
bin_split = bin_conv.split("b")
bin_num = bin_split[1]
print bin_num
#print "Binary numbers:"
for i in range(len(bin_num)):
    if (bin_num[i] is '1'):
        count = count + 1
        max_one_count = max(max_one_count, count)
    
    elif (bin_num[i] is '0'):
        count = 0 
    print count
    #print bin_num[i]

print "Consecutive ones=" + str(max_one_count)