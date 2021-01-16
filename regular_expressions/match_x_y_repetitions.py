# Question link: https://www.hackerrank.com/challenges/matching-x-y-repetitions/problem

"""
Task

You have a test S string .
Your task is to write a regex that will match S using the following conditions:

S should begin with 1 or 2 digits.
After that, S should have 3 or more letters (both lowercase and uppercase).
Then S should end with up to 3 . symbol(s). You can end with 0 to 3 . symbol(s), inclusively.

Test Cases:
12abcd - true
1abxc - true
1abxc. - true
abcd - false
11111sbsbsbs - false
3threeormorealphabets. - true
"""

Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{0,3}$'

import re

print(str(bool(re.search(Regex_Pattern, input("Enter the string: ")))).lower())