# coding: utf-8

__author__ = ["Samuel Joshua"]

"""
This program gets the RGB colors for the colors specified
"""

from PIL import ImageColor
# (255, 0, 0, 255)
print(ImageColor.getcolor('red', 'RGBA'))
# (255, 0, 0, 255)
print(ImageColor.getcolor('RED', 'RGBA'))
# (0, 0, 0, 255)
print(ImageColor.getcolor('Black', 'RGBA'))
# (210, 105, 30, 255
print(ImageColor.getcolor('chocolate', 'RGBA'))
