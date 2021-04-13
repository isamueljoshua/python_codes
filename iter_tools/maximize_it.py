# Problem st: hackerrank.com/challenges/maximize-it/problem

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
print("Cartesian PROD: ", len(list(product(*N))))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

# MY Failed solution

# from itertools import chain, combinations

# inpp = input("Enter k and m with space: ")
# k,m = inpp.split()

# fin_ls = []
# for ls in range(int(k)):
#     inp_val = input("Enter iter val:").split()
#     num_ls = inp_val[0]
#     # ls_val = ",".join(inp_val[1:])
#     ls_val = inp_val[1:]
#     fin_ls.append(ls_val)

# print("Final LS: ", fin_ls)
# # fin_ls1 = [x[:] for x in fin_ls]
# # print("FIN: ", fin_ls1)
# f_ls1 = list(chain(*fin_ls))
# print("Finn LS: ", f_ls1)

# fin_combs = list(combinations(f_ls1,int(k)))
# print("Combs: ", len(fin_combs))

# def appl_sq_sum(tupp):
#     sq_sum = 0
#     print("Current Tup:", tupp)
#     for val in tupp:
#         sq_val = pow(int(val),2)
#         sq_sum = sq_sum + sq_val
#         # print("SQ Sum: ", sq_sum)
#     return sq_sum

# summs_lst = []
# for i in fin_combs:
#     fn_sum = appl_sq_sum(i)
#     print("Final SUmm:", fn_sum)
#     summs_lst.append(fn_sum)

# print("FIN Sum Lst: ", summs_lst)
# print("MAX: ", max(summs_lst))

# modul = max(summs_lst) % int(m)
# print("Final modulo; ", modul)