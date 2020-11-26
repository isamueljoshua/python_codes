# coding: utf-8

__author__ = ["Samuel Joshua"]

from PIL import Image

im = Image.new('RGBA', (100,200), 'purple')
im.save('purpleImg.png')

# Invisible black, (0, 0, 0, 0), is the default color used if no color argument is specified
im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImg.png')