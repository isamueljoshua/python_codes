import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # this will give all lines in file that contain From:
    # if re.search('From:', line) :

    # this pattern will match strings which only start with From:
    # if re.search('^From:', line) :
    
    # the . (dot) character mathces any character in the string, either number or letter
    # if re.search('ˆF..m:', line) :
    
    # matches From: followed by one or more characters(".+") followed by an @ till the end of the line
    if re.search('^From:.+@', line):
        print (line)
