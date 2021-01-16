# Question link: https://www.hackerrank.com/challenges/matching-x-repetitions/problem

# Question asked for even digits, I didn't read that part :(
# Regex_Pattern = r'^(\w{40}([013579]|[\s]){5}){1}$'	# Do not delete 'r'.
Regex_Pattern = r'^[a-zA-z024860]{40}[13579\s]{5}$'

# x4202v2A22A9a6aaaaaa2G2222m222qwertyYuIo13957 - false since 9 is present in first 40 characters
# x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779 - false since length >45
# 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57 - true
import re

print(str(bool(re.search(Regex_Pattern, input("Enter the string: ")))).lower())