# coding: utf-8

__author__ = ["Samuel Joshua"]

from PIL import Image

catIm = Image.open('zophie.png')

catIm.rotate(90).save('rotated90.png')
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')

catIm.rotate(6).save('rotated6.png')
# The rotate() method has an optional expand keyword argument that can be set to True 
# to enlarge the dimensions of the image to fit the entire rotated new image
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')