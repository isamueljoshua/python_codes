# coding: utf-8

__author__ = ["Samuel Joshua"]

import string
def print_rangoli(size):
    width = 4 * size - 3
    print(width)
    alpha = string.ascii_lowercase
    # abcdefghijklmnopqrstuvwxyz
    print(alpha)
    # [2, 1, 0]
    print(list(range(size))[::-1])
    # [1, 2]
    print(list(range(1, size)))
    # [2, 1, 0, 1, 2]
    print(list(range(size))[::-1] + list(range(1, size)))
    for i in list(range(size))[::-1] + list(range(1, size)):
        # print()
        # 1
        # print(i)
        # c
        # print(alpha[size-1:i:-1])
        # bc
        # print(alpha[i:size])
        # print("Add both strs")
        # print(alpha[size-1:i:-1] + alpha[i:size])
        # print('-'.join(alpha[size-1:i:-1] + alpha[i:size]))
        # The center() method will center align the string, using a specified character (space is default) as the fill character
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))

size = int(input())
print_rangoli(size)