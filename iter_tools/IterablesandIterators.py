
# Other soln
from itertools import combinations
input()
combos = list(combinations(input().split(), int(input())))
count = 0
for i in combos:
    if "a" in i:
        count+=1
print(round(count/len(combos),3))


# My Wrong soln
# from itertools import combinations

# num_letters = int(input("Enter num letters: "))
# eng_letters = input("Enter Letters: ").split()
# num_indices = int(input("Enter number of indices: "))

# # print("Given Input")
# # print(num_letters)
# # print(eng_letters)
# # print(num_indices)

# enum_lst = list(enumerate(eng_letters, 1))
# # print()
# # print(enum_lst)

# indexes = [i[0] for i in enum_lst]
# # print()
# combinati = list(combinations(indexes, num_indices))
# print(combinati)

# a_indexes = []
# for i in enum_lst:
#     if i[1] == 'a':
#         # print("a found")
#         a_indexes.append(i[0])

# print("A Indexes: ", a_indexes)

# total_indexes = len(combinati)
# occourcance_counts = 0
# for i in a_indexes:
#     for c in combinati:
#         # print(c[0])
#         if i == c[0]:
#             print()
#             print("Found index")
#             print(c[0])
#             occourcance_counts += 1

# print("Final Counts: ", occourcance_counts)

# final_prob = occourcance_counts/total_indexes
# print("Final Probability: {0:.4f}".format(final_prob))