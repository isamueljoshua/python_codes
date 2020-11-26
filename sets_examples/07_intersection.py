# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
.intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).

Input:
The first line contains n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Output:
Output the total number of students who have subscriptions to both English and French newspapers.

5
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
en = input()
er = set(input().split())
fn = input()
fr = set(input().split())
print(len(er.intersection(fr)))
