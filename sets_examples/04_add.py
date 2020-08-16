"""
Task:
Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.

Find the total number of distinct country stamps.

Input:
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from

7
UK
China
USA
France
New Zealand
UK
France

Output:
Output the total number of distinct country stamps on a single line.

5
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
s = set()
for i in range(int(n)):
    ele = input()
    s.add(ele)

print(len(s))