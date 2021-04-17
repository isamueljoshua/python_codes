from itertools import groupby

def print_groupby(iterable, keyfunc=None):
    for k, g in groupby(iterable, keyfunc):
        print(k)
        print(g)
        print(list(g))
        print("key: '{}'--> group: {}".format(k, list(g)))
        
    # print([list(g) for k, g in groupby('AAAABBBCCD')])

print_groupby("1222311")

print("Last")
final_ls = [(len(list(g)), int(k)) for k, g in groupby(input("Enter the string: "), None)]
final_str = ""
for ele in final_ls:
    final_str = final_str + " " + str(ele)
    # print(final_str)
# print("Final STR")
print(final_str.strip())