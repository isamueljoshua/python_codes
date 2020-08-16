"""
.remove(x)
This operation removes element x from the set.
If element x does not exist, it raises a KeyError.
The .remove(x) operation returns None.

.discard(x)
This operation also removes element x from the set.
If element x does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

.pop()
This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError.

Input:
The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Output:
Print the sum of the elements of set s on a single line

4
"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())

# print(n)
# print(s)
# print(N)
for i in range(N):
    cmd = input().split()
    if s:
        if cmd[0] == 'pop':
            s.pop()
        elif cmd[0] == 'remove':
            s.remove(int(cmd[1]))
        elif cmd[0] == 'discard':
            s.discard(int(cmd[1]))
    else:
        break


# print("Final Set: ", s)
print(sum(s))