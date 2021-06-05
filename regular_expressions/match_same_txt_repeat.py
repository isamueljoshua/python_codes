# Problem location:
# https://www.hackerrank.com/challenges/matching-same-text-again-again/problem
# \group_number
# This tool (\1 references the first capturing group) matches the same text as previously matched by the capturing group.

"""

Example: 
regex: (\w)(\w)(\w)(\w)y\4\3\2\1
Input: malayalam
Output: true

Input: ab #1?AZa$ab #1?AZa$
Output: true
"""

Regex_Pattern = r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])(a|e|i|o|u|A|E|I|O|U)(\S)\1\2\3\4\5\6\7\8\9\10$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input("Enter the test string: ")))).lower())