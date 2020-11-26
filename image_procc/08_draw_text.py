# coding: utf-8

__author__ = ["Samuel Joshua"]

from PIL import Image, ImageDraw, ImageFont
import os

# After importing Image, ImageDraw, ImageFont, and os, we make an Image object for a new 200×200 white image 
# and make an ImageDraw object from the Image object
im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)
# We use text() to draw Hello at (20, 150) in purple
# We didn’t pass the optional fourth argument in this text() call, 
# so the typeface and size of this text aren’t customized.
draw.text((20, 150), 'Hello', fill='purple')


"""
To set a typeface and size, we first store the folder name (like /Library/Fonts) in fontsFolder. 
Then we call ImageFont.truetype(), passing it the .ttf file for the font we want, followed by an integer font size
"""
# On windows this is the path to all fonts ttf files
fontsFolder = 'C:\Windows\Fonts' # e.g. 'Library/Fonts'
# Store the Font object you get from ImageFont.truetype() in a variable like arialFont, 
# and then pass the variable to text() in the final keyword argument
arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
# The text() call at draws Howdy at (100, 150) in gray in 32-point Arial.
draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
im.save('draw_text.png')



"""
Good to know
Since it’s often hard to know in advance what size a block of text will be in a given font, the ImageDraw module also offers a textsize() method. 
Its first argument is the string of text you want to measure, and its second argument is an optional ImageFont object. 
The textsize() method will then return a two-integer tuple of the width and height that the text in the given font would be if it were written onto the image. 
You can use this width and height to help you calculate exactly where you want to put the text on your image.
"""
