# coding: utf-8

__author__ = ["Samuel Joshua"]

import re
def minion_game(string):
    stu = 0
    kev = 0

    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # if re.match()
    for i in range(len(string)):
        # why len(string)-i equals the number of times a word occurs in string
        # that is because, we need the number of words starting with either vowel or consonant. 
        # So, subtracting the index of the found 'vowel' in this case, 
        # gives us the number of words starting from that index with a vowel at first. Simple as that.
        """
        For the word "BANANA", the first vowel 'A' occurs at position 1, len("BANANA") = 6, 
        so there are 6-1 = 5 substrings starting with this letter 'A': ['A', 'AN', 'ANA', 'ANAN', 'ANANA'],
        you add one extra letter to that specific letter 'A' until you get to the end of the word.
        """
        print()
        print("i=", i)
        print(kev, stu)
        print("len of str: ", len(string))
        if string[i] in vowels:
            kev += len(string) - i
            print("Kevin current: ", kev)
        else:
            stu += len(string) - i
            print("Stuart current: ", stu)
    
    if stu > kev:
        print("Stuart"+" "+ "%d" % stu)
    elif stu < kev:
        print("Kevin"+" "+ "%d" % kev)
    else:
        print("Draw")


s = input("Enter string:")
minion_game(s)