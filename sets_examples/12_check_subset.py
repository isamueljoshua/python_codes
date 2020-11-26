# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Output:
True 
False
False
"""

ntest = int(input())

res_ls = []

for i in range(ntest):
    na = int(input())
    sA = set(input().split())
    nb = int(input())
    sB = set(input().split())

    print()
    print(na)
    print("Set A: ", sA)
    print(nb)
    print("Set B: ", sB)

    print(sA.issubset(sB))
    res_ls.append(str(sA.issubset(sB)))

    # SOln 2: print "True" if len(A) == len(B.intersection(A)) else "False"
    # SOln 3: 
    """
    for _ in range(int(input())):
        x, a, z, b = input(), set(input().split()), input(), set(input().split())
        print(a.issubset(b))
    """

print("\n".join(res_ls))