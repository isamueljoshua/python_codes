# Problem location: https://www.hackerrank.com/challenges/word-order/problem

"""
Input:
The first line contains the integer, n.
The next n lines each contain a word.

4
bcdef
abcdefg
bcde
bcdef

Output:
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

3
2 1 1
"""

from collections import OrderedDict

num_words = int(input("Enter number of words: "))

ord_dct = OrderedDict()
cnt = 1
for i in range(num_words):
    word_inp = input("Enter the word: ")
    if word_inp not in ord_dct.keys():
        ord_dct[word_inp] = 1
    else:
        ord_dct[word_inp] = ord_dct[word_inp] + 1

print("Final Dict: ", ord_dct)
print(len(ord_dct))
print(" ".join([str(v) for v in ord_dct.values()]))