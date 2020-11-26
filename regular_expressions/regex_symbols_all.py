# coding: utf-8

__author__ = ["Samuel Joshua"]

import re
hand = open('symbols_all.txt')
for line in hand:
    line = line.rstrip()
    
    # ^ matches line starting with From: till the end of the line
    # if re.search('^From:', line):
    # Output for above
    '''
    From:
    From: Sjah@gmc.com
    '''

    # $ Matches the end of the line
    # if re.search('From:$', line):
    # Output
    '''
    From:
    I am From:
    '''

    # . Matches any character (a wildcard)
    # if re.search('.',line):
    # Output
    '''
    From:
    I am From:
    From: Sjah@gmc.com
    sjdaahbd From: sjdcndcbhd
    '''

    # \s Matches a whitespace character
    # if re.search('\s',line):
    # Output
    '''
    I am From:
    From: Sjah@gmc.com
    sjdaahbd From: sjdcndcbhd
        ss
    '''

    # \S Matches a non-whitespace character (opposite of \s).
    if re.search('\S',line):
        # Output
        '''
        From:
        I am From:
        From: Sjah@gmc.com
        sjdaahbd From: sjdcndcbhd
            ss
        '''
        print (line)
