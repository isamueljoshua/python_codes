# coding: utf-8

__author__ = ["Samuel Joshua"]

import os

# deleting a file
# os.unlink('del_me.txt')

# to delete an empty directory
# else it gives an error - The directory is not empty: 'testdir'
# os.rmdir('testdir')

# if you still want to delete the entire folder
import shutil
# this does not throw an error like above
# so you must be careful with these functions
# shutil.rmtree('testdir')

'''
There is a module which sends to the recycle bin of your os
it is send2trash, you must do a pip install
'''
import send2trash
send2trash.send2trash('recycle_me.txt')