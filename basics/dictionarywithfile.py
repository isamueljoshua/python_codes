# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
Created on Fri Sep 22 12:36:34 2017
"""

# You can give sampledicttext.txt as file name
fname = input('Enter the file name:')
try:
    fhand=open(fname)
except Exception as e:
    print("Exception: ", e)
    print("File cannot be opened")
    exit()

counts=dict()
for line in fhand:
    words=line.split()
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1

print (counts)
"""
Output:
{'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}

"""

for line in fhand:
    words=line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
        
print ("\nUsing the get method now",counts)
"""
Output:
{'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}
"""