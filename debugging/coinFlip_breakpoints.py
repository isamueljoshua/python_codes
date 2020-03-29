'''
A breakpoint can be set on a specific line of code and forces the debugger to pause whenever the program execution reaches the line

'''

import random

heads = 0

for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')
    
print('Heads came up ' + str(heads) + ' times.')