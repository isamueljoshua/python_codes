# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:17:51 2017

@author: Administrator
"""

n=int(raw_input("Enter the number of records:"))

phone_book=dict()

for i in range(n):
    p_str=raw_input("Enter the name and phone_no:")
    #p_no=raw_input("Enter the phone number:")
    p_name=p_str.split()
    phone_book[p_name[0]]=p_name[1]

print phone_book
for i in range(n):
    query=raw_input("Enter a name to search:")

    
    if query in phone_book:
        print query+"="+phone_book[query]
        
    else:
        print "Not Found"
        