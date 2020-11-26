# coding: utf-8

__author__ = ["Samuel Joshua"]

# we use \ for file path in Wnidows
# for linux it is /

# the root folder for windows is C:\
# for Mac or linux it is /

# accessing windows files
# we use the \\ since python can consider \ for escape chars such as \n
'c:\\ssss\\exmapl.txt'
# or we can provide a raw string like
r'c:\sss\example.txt'

# example we have a list of files and folders
'\\'.join(['folder1', 'folder2', 'file.png'])

# now the above would work on windows, but we would want our program to work on all os'
# so, we can use the os module
import os

# this returns a string value for a path that is appropriate for the operating system you are running on
# output on windows folder1\folder2\folder3\file.png
# print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))

# to check the seperator being used
# output \
print(os.sep)

# to get current working dir
print(os.getcwd())

# to change directory
# os.chdir('C:\\')

'''
Absolute and relative file paths

Absolute file path - Always begins with the root folder e.g C:\\
C:\\folder1\\folder2\\folder3\\sample.png

Relative file path - Assumes always relative to the current folder
e.g if you specify sample.png then the program will look within this current folder

relative file path can also begin with folders like folder1\\folder2\\sample.png
In this case it assumes inside the root folder there is a folder1 and folder2 and then the file

'''
'''
The . and the .. folders

The . stands for this directory or this folder
The .. stands for parent folder 
'''

# the abspath() returns an absolute file path of the folder you are asking for
# output D:\files\sample.png
print(os.path.abspath('sample.png'))
# you can also specify it to look in the parent folders
# output D:\sample.png
print(os.path.abspath('..\sample.png'))

# the isabs() helps determine if something is an absolute file path or not
# it mainly looks for the root folder
# output - False
print(os.path.isabs('..\\folder1\\folder2\sample.png'))
# output - True
print(os.path.isabs('C:\\folder1\\folder2\sample.png'))

# the os.path.relpath() , gives the relative path between two paths you give it
# input is path to file, cur working directory path (starting point)
# output folder2\spam.png 
print(os.path.relpath('C:\\folder1\\folder2\\spam.png', 'C:\\folder1'))

# os.path.dirname('path') to retrieve the directory path
# output C:\folder1\folder2
print(os.path.dirname('C:\\folder1\\folder2\\spam.png'))

# os.path.basename('path') to retrieve the last folder/file name
# output - spam.png
print(os.path.basename('C:\\folder1\\folder2\\spam.png'))
# output - folder2
print(os.path.basename('C:\\folder1\\folder2'))

# os.path.exists to check the path exists
# output - False
print(os.path.exists('C:\\folder1\\folder2\\spam.png'))
# output - True , this is a windows calculator program
print(os.path.exists('C:\\windows\\system32\\calc.exe'))

# checking for file and folder names
# output - True
print(os.path.isfile('C:\\windows\\system32\\calc.exe'))
# output - False
print(os.path.isfile('C:\\windows\\system32'))
# output - True
print(os.path.isdir('C:\\windows\\system32'))
# output - False
print(os.path.isdir('C:\\windows\\system32\\calc.exe'))


# to get size in bytes as an integer
# output - 26112 bytes
print(os.path.getsize('C:\\windows\\system32\\calc.exe'))

# to list directory
# prints all the files and folder names inside the path given
print(os.listdir('C:\\windows\\system32'))

# to create new folders
os.makedirs('C:\\newtest\\example')