# Problem Location
# https://www.hackerrank.com/challenges/backreferences-to-failed-groups/problem

Regex_Pattern = r"^(-?)(\d\d)$"	# Do not delete 'r'.
Regex_Pattern = r"^(\d)+$"	# Do not delete 'r'.
Regex_Pattern = r"^(\-?)(\d)+$"	# Do not delete 'r'.
Regex_Pattern = r"^\d{2}(-?)(\d){2}\1(\d){2}\1\d{2}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input("Enter input string: ")))).lower())