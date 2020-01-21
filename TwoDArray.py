# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:42:53 2017

@author: Administrator
"""
# Function to calculate maximum sum in hourglass
def hourglass(arry):
    print arry
    hourglass_sum=[]
    hsum=0
    p1=1
    p2=2
    
    for i in xrange(4):
        for j in xrange(4):
            if (i<=4 and j<=4):    
                #print "Row1"
                print arr[i][j],arr[i][j+p1],arr[i][j+p2]
                #print "Row2"
                print arr[i+p1][j+p1]
                #print "Row3"
                print arr[i+p2][j],arr[i+p2][j+p1],arr[i+p2][j+p2]
                print "Done\n"
                hsum=arr[i][j]+arr[i][j+p1]+arr[i][j+p2]+arr[i+p1][j+p1]+arr[i+p2][j]+arr[i+p2][j+p1]+arr[i+p2][j+p2]
                print "Hsum="+str(hsum)
                hourglass_sum.append(hsum)
            else: print "Out of range"
    print "Maximum Sum="
    print max(hourglass_sum)
    #pass

arr = []
print arr
#print "Welcome to 2d Arrays"
for arr_i in xrange(6):
    #for arr_j in range(6):
    arr_temp = map(int,raw_input("Enter each row elements with a space:").strip().split(' '))
        #arr = [[arr_temp for x in xrange(6)] for y in xrange(6)]
    arr.append(arr_temp)

hourglass(arr)
