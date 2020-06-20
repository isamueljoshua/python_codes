'''
Plain text files - when you open them you can read their content easily
Binary files - when you open these types of files, it is impossible to understand (e.g exe, pdf)
'''

helloFile = open('hello.txt')
# file data type has several methods, let's see read method
content = helloFile.read()
# read method returns all contents of file as a single string
print(content)
helloFile.close()

# alternatively there are readlines() for file objects
# returns all lines as a list of strings
helloFile = open('hello.txt')
# output - ['Hello world\n', 'How are you?']
print(helloFile.readlines())
helloFile.close()


# WRITE content to a file
# write mode overwrites all content of a file, else creates a new file
# append mode appends to the end of the file, also creates a file if it does not exist already
helloFile = open('hello2.txt', 'w')
# write method also returns the number of bytes it wrote into the file
helloFile.write('Hello!!!!!')
helloFile.write('Hello!!!!!')
helloFile.write('Hello!!!!!')
helloFile.close()

# another example
baconFile = open('bacon.txt', 'w')
baconFile.write('bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nbacon is delicious.')
baconFile.close()


'''
To store variables that have lists, dictionaries and other complex data structures
we can store these to shelf files
'''
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['A', 'B', 'C', 'D']
# this data is stored in 3 binary files on windows
# mydata.bak, mydata.dat, mydata.dir
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
shelfFile.close()

# just like a python file, we can access keys and values
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))

print(list(shelfFile.values()))