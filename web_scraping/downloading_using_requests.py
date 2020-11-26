# coding: utf-8

__author__ = ["Samuel Joshua"]

import requests

# to know more about requests module: https://requests.readthedocs.io/en/master/
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print("Status Code")
print(res.status_code)
print("Total chars in file")
print(len(res.text))
print("First 500 texts")
print(res.text[:500])


# we are writing in binary code thought the url has a text file in order to maintain unicode encoding of the text
# to know more abt unicode: https://nedbatchelder.com/text/unipain.html
playFile = open('RomeoJuliet.txt', 'wb')
# iter_content returns the chunk of the data on each iteration in the loop
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()


badres = requests.get('https://automatetheboringstuff.com/bsdhsbdhbs')
# this raises a python error and shows if the file is not found
print("Raise for Status:")
print(badres.raise_for_status())