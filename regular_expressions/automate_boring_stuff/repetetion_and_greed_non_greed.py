import re

# ? character - match the preceding group 0 or 1 times - optional can appear once or not appear at all
# batRegex = re.compile(r'Batman|Batwoman')
# a much shorter version of the above can be
# the ? here says the group wo can appear in the text 0 or 1 times
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
# prints Batman
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
# prints Batwoman
print(mo.group())

mo = batRegex.search('The Adventures of Batman and Batwoman')
# prints Batman only since re.search returns on first match
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowowman')
# returns None since the regex will match only 0 or 1 occourances only
print(mo==None)

# let's make the area code of this phone number optional by grouping it and putting a question mark
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
message = 'Call me at 415-555-1011 or at 222-333-1111'
mo = phoneRegex.search(message)
# returns the first matched phone number
print(mo.group())
message = 'Call me at 555-1011'
mo = phoneRegex.search(message)
# also returns the first matched phone number without the area code
print(mo.group())

# another option is to escape the question mark with the \ , which means we are looking for the question mark in the string, 
# below is an example
dinrRegex = re.compile(r'dinner\?')
mo = dinrRegex.search('Did you have dinner?')
# prints dinner?
print(mo.group())


'''
Next let's look at the * in regex
* means the pattern or group preceding the * can appear 0 or more times
'''
print("\nUsing the * expression to match")
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
# prints Batman
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
# prints Batwoman
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowoman')
# prints Batwowowoman 
print(mo.group())


'''
Next let's look at the + in regex
+ means the pattern or group preceding the + must appear 1 or more times
'''
print("\nUsing the + expression to match")
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
# returns None since the group wo must appear 1 or more times
print(mo == None)

mo = batRegex.search('The Adventures of Batwoman')
# prints Batwoman as wo matched 1 time
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowoman')
# prints Batwowowoman as wo matched more than 1 time
print(mo.group())


'''
escaping all the characters we have seen above
'''
print("\nEscaping the ? * and + while matching")
escregex = re.compile(r'\+\*\?')
mo = escregex.search('I learnt about +*? today')
# matches the +*? chaaracters that were matched
print(mo.group())
# we can also group them to match 1 or more times
escregex = re.compile(r'(\+\*\?)+')
mo = escregex.search('I learnt about +*?+*?+*?+* today')
# matches the +*?+*?+*? chaaracters that were matched
print(mo.group())


'''
let's say we wanted to match a specific munber of repetetions, like 2 or 3 or 4
'''
print("\nExactly matching custom number of times with the {}")
haRegex = re.compile(r'(Ha){3}')
# you could have also written the above regex as haRegex = re.compile(r'HaHaHa')
mo = haRegex.search('He said "HaHaHa"')
# prints HaHaHa
print(mo.group())
mo = haRegex.search('He said "HaHa"')
# returns None since we have specified we want to match 3 repetetions only
print(mo==None)

# let's look at the below phone number regex, 
# expl: match phone numbers whose area code is optional and come in a string 3 times, optionally seperated by a comma
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
message = 'Call me at 415-555-1011,333-1111,000-333-1111'
mo = phoneRegex.search(message)
print(mo.group())

'''
Using the above method but let's match a range of repetetions
{x, y} - at least x, at most y
'''
print("\nExactly matching custom number of times with the {x,y} - at least x, at most y")
haRegex = re.compile(r'(Ha){3,5}')
# you could have also written the above regex as haRegex = re.compile(r'HaHaHa')
mo = haRegex.search('He said "HaHaHa"')
# prints HaHaHa
print(mo.group())
mo = haRegex.search('He said "HaHaHaHaHa"')
# prints HaHaHaHaHa
print(mo.group())
mo = haRegex.search('He said "HaHaHaHaHaHaHa"')
# prints HaHaHaHaHa only 5 of the Ha since we have set the upper limit to 5
print(mo.group())

# the below regex means 0 to 5
# haRegex = re.compile(r'(Ha){,5}')

# the below regex means 3 or more
# haRegex = re.compile(r'(Ha){3,}')

# let's experiment
# match string of digits between 3 and 5 of them
digitRegex = re.compile(r'(\d){3,5}')
# the above regex matches the first 5 numbers and returns 12345
# but if you notice it could have just matched the first 3 characters or 4 characters,
# instead it matched the first 5 characters, that's because by deafult regex in python do greedy matches
# which means it tries to match the longest possible string
print(digitRegex.search('1234567890'))

# so let's do a non-greedy match
digitRegex = re.compile(r'(\d){3,5}?')
# now it matches only 123, so it has matched the smallest possible string
print(digitRegex.search('1234567890'))
