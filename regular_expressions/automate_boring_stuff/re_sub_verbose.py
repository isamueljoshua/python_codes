# we can find and replace some text with regular expression as well.

import re
namesRegex = re.compile(r'Agent \w+')
# output - ['Agent Alice', 'Agent Bob']
print(namesRegex.findall('Agent Alice gave some docs to Agent Bob.'))

# sub fnids and replaces all occourance of the matched regex with the word REDACTED
# output - REDACTED gave some docs to REDACTED.
print(namesRegex.sub('REDACTED','Agent Alice gave some docs to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*')
# this matches only what's in the group
# output - ['A', 'B']
print(namesRegex.findall('Agent Alice gave some docs to Agent Bob.'))

# next, we will use \1 to replace only the char of element from the group
# output - Agent A***** gave some docs to Agent B*****.
print(namesRegex.sub(r'Agent \1*****','Agent Alice gave some docs to Agent Bob.'))

'''
Verbose formatting using re.VERBOSE

In the verbose mode, we can specify regex in multiple lines,
also, we can give comments inside the regex itself
this makes the regex more readable
'''
re.compile(r'''
\d\d\d   # area code
-        # first dash
\d\d\d   # first 3 digits
-        # second dash
\d\d\d\d # last 4 digits''', re.VERBOSE)

re.compile(r'''
(\d\d\d-)|   # area code (without parenthesis and with dash)
(\(\d\d\d\)) # -or- area code (with parenthesis and withot dash)
\d\d\d   # first 3 digits
-        # second dash
\d\d\d\d # last 4 digits''', re.VERBOSE)

# passing multiple options
re.compile(r'''
(\d\d\d-)|   # area code (without parenthesis and with dash)
(\(\d\d\d\)) # -or- area code (with parenthesis and withot dash)
\d\d\d   # first 3 digits
-        # second dash
\d\d\d\d # last 4 digits''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
