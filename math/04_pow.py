"""
Problem source: https://www.hackerrank.com/challenges/python-power-mod-power/problem
Powers or exponents in Python can be calculated using the built-in power function. Call the power function a^b as shown below:
pow(a,b)
It's also possible to calculate a^b mod m
pow(a,b,m)

Note: math.pow() does not take m as argument
"""

a, b, m = int(input()), int(input()), int(input())

print(pow(a,b))
print(pow(a,b,m))