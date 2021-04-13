# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

nst = int(input("Enter the number of Students: "))
inp_cols = input("Enter col names: ")
Student = namedtuple('Student', inp_cols.split())
print(Student)
print(dir(Student))
scores = [Student(*input().split()).MARKS for i in range(nst)]
print(scores)
print("Average: ")
print(sum(map(int, scores))/nst)

# total = 0
# for i in range(nst):
#     v = input("Enter the values: ").split()
#     print(v)
#     # marks = Student().MARKS
#     # total = total + marks
# print("Total: ", total)