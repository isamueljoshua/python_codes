# coding: utf-8

__author__ = ["Samuel Joshua"]

import re
hand = open('mbox-sh.txt')
for line in hand:
    line = line.rstrip()
    '''
    we want lines that start with “X-”, followed by
    zero or more characters (“.*”), followed by a colon (“:”) and then a space. After
    the space we are looking for one or more characters that are either a digit (0-9)
    or a period “[0-9.]+”. Note that inside the square brackets, the period matches an
    actual period (i.e., it is not a wildcard between the square brackets)
    '''
    # if re.search('^X\S*: [0-9.]+', line) :
    #     print(line)
    # Output
    '''
    X-DSPAM-Confidence: 0.8475
    X: 0.8475
    X-DSPAM-Conf: 0.8475
    '''

    # strict match using findall() and the parenthesis () to get the number only from the match
    x = re.findall('^X\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)
    # Output
    '''
    ['0.8475']
    ['0.8475']
    ['0.8475']
    '''