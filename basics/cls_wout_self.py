# coding: utf-8

__author__ = ["Samuel Joshua"]

# For more explanation, refer here: https://stackoverflow.com/a/62489103/9197808

class A:
    # Class calls method directly since it assumes as a static method
    def a():
        print("Without self calling me" )


A.a()

# This kind of call below fails since it passes the self keyword to the method,
# But if you declare the a() function with @staticmethod it will work
"""
Traceback (most recent call last):
  File "d:\kkk\PythonPrograms\Samplepgms\basics\cls_wout_self.py", line 15, in <module>
    ca.a()
TypeError: a() takes 0 positional arguments but 1 was given
"""
ca = A()
ca.a()