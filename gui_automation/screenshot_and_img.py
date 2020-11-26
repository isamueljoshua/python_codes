# coding: utf-8

__author__ = ["Samuel Joshua"]

# pyautogui uses pillow, using pillow and image based programs can be found at automatetheboringstuff.com/chapter17
# for linux systems the scrot must be installed with sudo apt-get install scrot
# on windows the above step is not required

import pyautogui

# returns the image object, which is described in pillow docs
print(pyautogui.screenshot())

# to save the screenshot, pass it a path
# pyautogui.screenshot('D:\sams\PythonPrograms\Samplepgms\gui_automation\screenshot_example.png')

# to locate an image on screen use, it returns the x and y coordinates of where it found the image similar to the source provided
# returns a tuple of 4 elements, the x and y coordinates of where it found the match, the width and height of that region
print(pyautogui.locateOnScreen('path_to_calc7key.png'))

# locate the center coordinates of the match
print(pyautogui.locateCenterOnScreen('path_to_calc7key.png'))

# move the mouse to the coordinates previously found
pyautogui.moveTo((1492, 565), duration=1)
# then you can also click on it as well
# click can be passed with a tuple or we can pass integers in parameters
pyautogui.click((1492, 565))
pyautogui.click(1492, 565)

'''
Note on the locate functions
1. Computationally expensive, depending on the size of your screen, they can take up to a full second to execute this function
so you really can't use it in real time games and the screen is constantly refreshing.
2. Image matches have to be pixel perfect, every single pixel color here in sample image has to match the screen to find

You can check out the documentation of pyautogui to speed up this and alos finding partial matches
'''

# A bot created by the instructor of this course to play the flash game sushigoround
# sushigoroundbot - can find on github page at asweigart/sushigoroundbot