import re

message = 'Call me at 415-555-1011 or at 222-333-1111'

# here now er create groups using parenthesis on the regex
phoneNumbers = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# regular exp datatype has a search method which returns a match objcet
mo = phoneNumbers.search(message)

print(mo.group())

# now since we created groups in regex we can find them using
# this gives output as 415
print(mo.group(1))
# this gives output as 555-1011
print(mo.group(2))

# now let us try to find paranthesis in our pattern
msg_paran = 'My phone number is (415) 555-1011'
# to do that put a \ in front of the regex bracket and before the end
phoneNumbers = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumbers.search(msg_paran)
# print(mo)
print(mo.group())

# experiment - match the paranthesis as well as create a group of matched patterns
phoneNumbers = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumbers.search(msg_paran)
# print(mo)
print("output of grouping the matched paranthesis")
print(mo.group())
# output (415)
print(mo.group(1))
# output 555-1011
print(mo.group(2))


'''
PIPE CHARACTERS
E.g you want to match Batman, Batmobile or Bat, we can use pipes
'''
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
# returns Batmobile as output
print(mo.group())
# returns only mobile as output since it matched that suffix
# print(mo.group(1))

# returns None if the pattern does not match
mo = batRegex.search('Batmototcycle lost a wheel')
print(mo)