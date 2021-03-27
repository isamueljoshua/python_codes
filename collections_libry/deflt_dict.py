# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

# we must append indexes to the list
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1,n+1):
    d[input()].append(str(i))
    
# print("Current D", d)
for i in range(m):
    print (' '.join(d[input()]) or -1)


# Tutorial + Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Here below is my solution, but somehow HackerRank marks it as failed for the inputs attached
# d = defaultdict(list)

# inp = input("Enter N and M: ").split()
# n, m = inp
# print("N: ", n)
# print("M: ", m)

# for i in range(int(n)):
#     d['A'].append(input("Enter group A vals: "))

# for i in range(int(m)):
#     d['B'].append(input("Enter group B vals: "))

# final_dct = defaultdict(list)

# for val in d['B']:
#     print("\nCurrent Val: ")
#     print(val)

#     if val not in d['A']:
#         final_dct[val].append(-1)

#     for index in range(len(d['A'])):
#         print(index)
#         print("Actual Value:")
#         print(d['A'][index])
#         if d['A'][index] == val:
#             print("MATCH!!")
#             final_dct[val].append(index+1)

# print("The Final Dict: ")
# print(final_dct)

# for k,v in final_dct.items():
#     # print(k)
#     print(" ".join(map(str,v)))