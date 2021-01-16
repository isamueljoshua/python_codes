# Question link: https://www.hackerrank.com/challenges/matching-ending-items/problem

"""
Task

Write a RegEx to match a test string, S , under the following conditions:

S should consist of only lowercase and uppercase letters (no numbers or symbols).
S should end in s.

Test cases:
s - false (since starting letters must occour)
12s - false
Kites - true
(one)1ess - false
"""

Regex_Pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input("Enter the string: ")))).lower())