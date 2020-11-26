# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
.symmetric_difference()
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

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
Output total number of students who have subscriptions to the English or the French newspaper but not both.

8
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
en = input()
er = set(input().split())
fn = input()
fr = set(input().split())
# O/P {'11', '21', '5', '55', '10', '7', '4', '9'}
print(er.symmetric_difference(fr))
print(len(er.symmetric_difference(fr)))