# coding: utf-8

__author__ = ["Samuel Joshua"]

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # this will give all lines in file that contain From:
    # if re.search('From:', line) :
    # Output
    '''
    From: from
    From:sks@examplecom
    We are coming From:skssajnd@example.com
    '''

    # this pattern will match strings which only start with From:
    # if re.search('^From:', line) :
    # Output
    '''
    From: from
    From:sks@examplecom
    '''
    
    # the . (dot) character matches any character in the string, either number or letter
    # if re.search('^F..m:', line) :
    # Output
    '''
    From: from
    From:sks@examplecom
    F@!m:
    '''
    
    # matches From: followed by one or more characters(".+") followed by an @ till the end of the line
    if re.search('^From:.+@', line):
        # Output
        '''
        From:sks@examplecom
        '''
        print (line)
