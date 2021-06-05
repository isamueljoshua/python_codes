# Problem Location
# https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem

"""
Input:12345678
Output: true

Input:12-34-56-87
Output: true

Input:1-234-56-78
Output: false

Input:12-45-7810
Output: false
"""
# Regex_Pattern = r"^(-?)(\d\d)$"	# Do not delete 'r'.
# Regex_Pattern = r"^(\d)+$"	# Do not delete 'r'.
# Regex_Pattern = r"^(\-?)(\d)+$"	# Do not delete 'r'.

# Final method:
# to check your regex with sample input, can run this file or 
# use https://www.debuggex.com/
Regex_Pattern = r"^\d{2}(-?)(\d){2}\1(\d){2}\1\d{2}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input("Enter input string: ")))).lower())