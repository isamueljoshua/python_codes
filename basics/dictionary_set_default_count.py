# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
Program to count number of characters in the string
Output - {'I': 2, 'T': 1, ' ': 6, 'W': 1, 'A': 4, 'S': 1, 'C': 1, 'O': 1, 'L': 1, 'D': 2, 'Y': 2, 'N': 1, 'M': 1}
"""

message = 'It was a cold Day in May'

count = {}

# this code without upper() would seperately give caps D and small d's count, so modifying it
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)