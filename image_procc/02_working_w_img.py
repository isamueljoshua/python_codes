# coding: utf-8

__author__ = ["Samuel Joshua"]

from PIL import Image

catIm = Image.open('zophie.png')
# 816, 1088
print(catIm.size)

width, height = catIm.size
# 816
print(width)
# 1088
print(height)
# zophie.png
print(catIm.filename)
# PNG
print(catIm.format)
# Portable network graphics
print(catIm.format_description)
# saving the image in jpg format
catIm.save('zophie.jpg')