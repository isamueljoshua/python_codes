# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
.update() or |=
Update the set by adding elements from an iterable/another set.

.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.
"""

H = set("Hacker")
R = set("Rank")
H.update(R)
# O/P set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
print (H)

H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
# O/P {'a', 'k'}
print (H)

H = set("Hacker")
R = set("Rank")
H.difference_update(R)
# O/P {'H', 'r', 'e', 'c'}
print (H)

H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
# O/P {'H', 'r', 'e', 'c', 'n', 'R'}
print (H)


"""
Input:
The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2*N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

Output:
Output the sum of elements in set A.
38
"""

nA = input()
# print(nA)
A = set(input().split())
# print(A)

n = int(input())
# print(n)
for i in range(n):
    op, nB = input().split()
    B = set(input().split())
    if op == "update":
        A.update(B)
    elif op == "intersection_update":
        A.intersection_update(B)
    elif op == "difference_update":
        A.difference_update(B)
    elif op == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    else:
        continue

# print("Output: ")
# print(A)
# print("Final Sum: ")
print(sum(list(map(int, A))))