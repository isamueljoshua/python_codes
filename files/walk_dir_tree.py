# coding: utf-8

__author__ = ["Samuel Joshua"]

# to walk a directory os provides a os.walk() method
import os

# returns 3 values on each iteration

for folderName, subfolders, filenames in os.walk('testdir'):
    print("The folder is " + folderName)
    print("The subfolders in " + folderName + " are: " + str(subfolders))
    print("The filenames in " + folderName + " are: " + str(filenames))
    print()
