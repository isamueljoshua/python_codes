# Problem Location: hackerrank.com/challenges/capturing-non-capturing-groups/problem

"""
Note: (?: ) can be used to create a non-capturing group. It is useful if we do not need the group to capture its match. e.g (ok)?:

Input:
hiokokok - true (output)
hisoksokdok - false (output)
sssadsd - false (output)
"""

Regex_Pattern = r'(ok){3,}'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input("Enter your String: ")))).lower())