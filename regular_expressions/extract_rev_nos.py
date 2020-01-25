import re
hand = open('rev_nos.txt')
for line in hand:
    line = line.rstrip()
    '''
    looking for lines that start with “Details:”,
    followed by any number of characters (“.*”), followed by “rev=”, and then
    by one or more digits. We want to find lines that match the entire expression but
    we only want to extract the integer number at the end of the line, so we surround
    “[0-9]+” with parentheses
    '''
    x = re.findall('^Details:.*rev=([0-9]+)', line)
    if len(x) > 0:
        print (x)

'''
Note:
Remember that the “[0-9]+” is “greedy” and it tries to make as large a string of
digits as possible before extracting those digits. This “greedy” behavior is why we
get all five digits for each number. The regular expression library expands in both
directions until it encounters a non-digit, or the beginning or the end of a line.
'''

# Output:
'''
['39772']
['39888']
['39000']
'''