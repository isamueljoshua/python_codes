import re

message = 'Call me at 415-555-1011 or at 222-333-1111'

# getting a regex object, we pass a raw string, it is just a regular string, when we use a \ in a string it does not consider it to be a escape character like \m
phoneNumbers = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# regular exp datatype has a search method which returns a match objcet
mo = phoneNumbers.search(message)

# tells you the actual text (first occourence)
# Output 415-555-1011
print(mo.group())

'''
To find every occourence of the pattern use the findall()
'''
# O/P ['415-555-1011', '222-333-1111']
print(phoneNumbers.findall(message))
