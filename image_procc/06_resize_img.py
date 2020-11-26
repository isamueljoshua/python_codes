# coding: utf-8

__author__ = ["Samuel Joshua"]

from PIL import Image

catIm = Image.open('zophie.png')

width, height = catIm.size
quartersizedIm = catIm.resize((int(width/2)), (int(height/2)))
quartersizedIm.save('quartersized.png')

saveIteIm = catIm.resize((width, height + 300))
saveIteIm.save('saveIte.png')