import shutil

# copies the text file from one location to another
# this returns a file path where the file is copied, but we can ignore it
shutil.copy('D:\\sams\\PythonPrograms\\Samplepgms\\files\\bacon.txt', 'D:\\sams\\PythonPrograms\\Samplepgms\\')

# we can copy and rename using the same function by specifying the file name as well
shutil.copy('D:\\sams\\PythonPrograms\\Samplepgms\\files\\bacon.txt', 'D:\\sams\\PythonPrograms\\Samplepgms\\copied_bacon.txt')

# to copy an entire folder we can use the copytree
shutil.copytree('D:\\sams\\PythonPrograms\\Samplepgms\\files\\testdir', 'D:\\sams\\PythonPrograms\\Samplepgms\\files\\testdir_bkp')

# move a file to a new location
shutil.move('D:\\sams\\PythonPrograms\\Samplepgms\\copied_bacon.txt', 'D:\\sams\\PythonPrograms\\Samplepgms\\files\\')

# to rename there isn't a rename function, instead we use the move function
# specify from file path and give same path but new file name to rename
shutil.move('D:\\sams\\PythonPrograms\\Samplepgms\\files\\copied_bacon.txt', 'D:\\sams\\PythonPrograms\\Samplepgms\\files\\renamed_bacon.txt')

