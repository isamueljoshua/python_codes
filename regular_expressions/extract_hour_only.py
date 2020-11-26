# coding: utf-8

__author__ = ["Samuel Joshua"]

import re
hand = open('rev_nos.txt')
for line in hand:
    line = line.rstrip()
    '''
    looking for lines that start
    with “From ” (note the space), followed by any number of characters (“.*”), followed
    by a space, followed by two digits “[0-9][0-9]”, followed by a colon character.
    This is the definition of the kinds of lines we are looking for.
    
    In order to pull out only the hour using findall(), we add parentheses around
    the two digits as follows
    '''
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0 : print (x)


# Output
'''
['09']
['10']
['00']
'''