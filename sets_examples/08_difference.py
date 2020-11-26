# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
.difference()
The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).

Input:
The first line contains the number of students who have subscribed to the English newspaper.
The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
The third line contains the number of students who have subscribed to the French newspaper.
The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Output:
Output the total number of students who are subscribed to the English newspaper only.

4
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
en = input()
ne = set(input().split())
ef = input()
nf = set(input().split())
# O/P {'5', '4', '7', '9'}
print(ne.difference(nf))
print(len(ne.difference(nf)))
