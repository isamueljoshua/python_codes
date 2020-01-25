# import re
# s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
# # findall returns a list of the matched strings
# lst = re.findall('\S+@\S+',s)
# print(lst)


'''
Reading and mathcing from a file
'''
import re
hand = open('mail_addresses.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    # output
    '''
    ['stephen.marquard@uct.ac.za']
    ['<postmaster@collab.sakaiproject.org>']
    ['<source@collab.sakaiproject.org>;']
    ['apache@localhost)']
    '''

    # to choose what characters must match we use the [] (square brackets)
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    '''
    Explanation for the above re:
    we are looking for substrings that start with a single lowercase letter,
    uppercase letter, or number “[a-zA-Z0-9]”, followed by zero or more non-blank
    characters (“\S*”), followed by an at-sign, followed by zero or more non-blank
    characters (“\S*”), followed by an uppercase or lowercase letter. Note that we
    switched from “+” to “*” to indicate zero or more non-blank characters since “[azA-
    Z0-9]” is already one non-blank character. Remember that the “*” or “+”
    applies to the single character immediately to the left of the plus or asterisk.
    '''
    # output
    '''
    ['stephen.marquard@uct.ac.za']
    ['postmaster@collab.sakaiproject.org']
    ['source@collab.sakaiproject.org']
    ['apache@localhost']
    '''
    if len(x) > 0 :
        print (x)
