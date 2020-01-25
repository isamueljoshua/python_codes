import re
x = 'We just received $10.00 for cookies.'
'''
Since we prefix the dollar sign with a backslash, it actually matches the dollar sign
in the input string instead of matching the “end of line”, and the rest of the regular
expression matches one or more digits or the period character. Note: Inside square
brackets, characters are not “special”. So when we say “[0-9.]”, it really means
digits or a period. Outside of square brackets, a period is the “wild-card” character
and matches any character. Inside square brackets, the period is a period
'''
y = re.findall('\$[0-9.]+',x)
print(y)

# Output
'''
['$10.00']
'''