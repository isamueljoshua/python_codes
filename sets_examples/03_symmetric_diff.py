"""
Input:
The first line of input contains an integer, M.
The second line contains M  space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output:
Output the symmetric difference integers in ascending order, one per line.

sample Input:
4
2 4 5 9
4
2 4 11 12

Output:
5
9
11
12
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_m = input()
m=set(list(map(int, input().split())))
num_n = input()
n=set(list(map(int, input().split())))

diff_m = m.difference(n)
diff_n = n.difference(m)
# print("set1 union",diff_m.sort())
# O/P {9, 5}
# print(diff_m)
# O/P {11, 12}
# print(diff_n)
final_union = diff_m.union(diff_n)
# O/P {9, 11, 12, 5}
# print(final_union)
final_int_ls = list(final_union)
# O/P [9, 11, 12, 5]
# print(final_int_ls)
# print(type(final_int_ls))
final_int_ls.sort()
# for i in final_int_ls:
#     print(i)
# fs = final_int_ls.sort()
# print("Sort List: ", fs)
final_ls = list(map(str, final_int_ls))
print("\n".join(final_ls))
