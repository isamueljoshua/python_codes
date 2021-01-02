"""
This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Input:
Enter the actual str and num of subsequesces: HACK 2

Output:
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

inp = input("Enter the actual str and num of subsequesces: ")
src, iters  = inp.split()
src = ''.join(sorted(src))
comb_ls = list(combinations_with_replacement(src, int(iters)))
n_ls = ["".join(i) for i in comb_ls]
print("\n".join(n_ls))