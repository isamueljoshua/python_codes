# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
.union()

The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

Input:
The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Output:
Output the total number of students who have at least one subscription.
13

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
ne = int(input())
se = set(input().split())
nf = int(input())
sf = set(input().split())

print(len(se.union(sf)))