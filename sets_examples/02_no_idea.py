# coding: utf-8

__author__ = ["Samuel Joshua"]

"""Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Input:
3 2
1 5 3
3 1
5 7

Output:
1

Explanation

You gain 1 unit of happiness for elements 3 and 1 in set A. You lose 1 unit for 5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1=1.
"""
n, m = (int(i) for i in input().split())
l = map(int, input().strip().split(' '))
a = set(map(int, input().strip().split(' ')))
b = set(map(int, input().strip().split(' ')))
result = 0
for i in l:
    if i in a:
        result += 1
    if i in b:
        result += -1
print(result)
