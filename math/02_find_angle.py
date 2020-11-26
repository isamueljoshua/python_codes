# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
For this Hackerrank problem refer: https://www.hackerrank.com/challenges/find-angle

SOH...
Sine: sin(θ) = Opposite / Hypotenuse
...CAH...
Cosine: cos(θ) = Adjacent / Hypotenuse
...TOA
Tangent: tan(θ) = Opposite / Adjacent

# Soln:
We can Solve this problem by using a property: 
** That a median on the hypotenuse divides the right angled triangle in two isoceles triangle.
** * Means AM=BM=CM * So, ∡MBC = ∡MCB

"""
import math
ab = int(input("Enter AB"))
bc = int(input("Enter BC"))

degree_sign= u'\N{DEGREE SIGN}'
# print(degree_sign)
print(str(int(round(math.degrees(math.atan2(ab,bc))))) + degree_sign)

# print(ab ** 2)
# print(bc ** 2)
# ac = math.sqrt((ab ** 2) + (bc ** 2))
# print("AC=", ac)
# M  = ac/2
# print("M", M)

# # applying tan(θ) = Opposite / Adjacent
# tnthetha = M / bc
# print("Tan Theta" ,tnthetha)
# taninverse = math.atan(tnthetha)
# print("Tan Inverse", taninverse)

# taninverse_degrees = math.degrees(taninverse)
# print("Tan Inverse Degrees", taninverse_degrees)