"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.
"""
sA = set(input().split())
print(sA)
nOther = int(input())
print(nOther)
res_ls = []
for i in range(nOther):
    sB = set(input().split())
    print(sB)
    print(sA>sB)
    res_ls.append(sA>sB)

# O/P [True, False]
print(res_ls)
# O/P False
print(all(res_ls))