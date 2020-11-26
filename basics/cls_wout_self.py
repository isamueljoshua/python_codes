# coding: utf-8

__author__ = ["Samuel Joshua"]

class A:
    def a():
        print("Without class calling me")

A.a()

# this kind of declaration fails since it passes the self keyword to the method
ca = A()
ca.a()