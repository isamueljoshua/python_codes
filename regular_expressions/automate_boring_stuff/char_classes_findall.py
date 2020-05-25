import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex)

# returns a list with all matched strings
# output of below match is ['415-555-1011', '000-333-1111']
print(phoneRegex.findall('Call me at 415-555-1011,333-1111,000-333-1111'))

# If we create groups in the phone number regex, then we get list of tuples with the matched groups
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# output of below is [('415', '555-1011'), ('000', '333-1111')
print(phoneRegex.findall('Call me at 415-555-1011,333-1111,000-333-1111'))

# we can create a larger group around the existing groups
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
# output is [('415-555-1011', '415', '555-1011'), ('000-333-1111', '000', '333-1111')]
print(phoneRegex.findall('Call me at 415-555-1011,333-1111,000-333-1111'))

'''
Character classes
'''
# \d is a character class that signifies digit
# for more info, refer to the table 7-1 here: http://automatetheboringstuff.com/2e/chapter7/

# let's now take an example
# 12 days of Christmas
lyrics = '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
xmasRegex = re.compile(r'\d+\s\w+')
# output is ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
print(xmasRegex.findall(lyrics))


'''
Making your own character classes
'''
# same as saying r'(a|e|i|o|u)' or you can also put r[a-z] means all chars from a to z
# you can also specify r[a-zA-Z] which means it will match the capital letters as well.
vowelRegex = re.compile(r'[aeiouAEIOU]')
# output is ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']
print(vowelRegex.findall('Robocop eats baby food'))

# find just two in a row
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
# output is ['ea', 'oo']
print(doubleVowelRegex.findall('Robocop eats baby food'))

'''
Negative Character classes
add a ^ to match the pattern that isn't in the character class
'''
constantsRegex = re.compile(r'[^aeiouAEIOU]')
# output is ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']
print(constantsRegex.findall('Robocop eats baby food.'))