import pyautogui

# all screen's pointer positon is (0,0) at top left corner and max at bottom right corner
# my screen resolution is 1920 * 1080 so my max is (1920*1080)

# get your monitor screen's resolution (width and height)
print(pyautogui.size())
# just fetching the resolution in two different variables
width, height = pyautogui.size()
print(width)
print(height)

# current position of mouse cursor
print(pyautogui.position())

# to move the mouse cursor to a position
pyautogui.moveTo(10,10)

# the above moves the mouse very quickly, to do it slowly
pyautogui.moveTo(10,80, duration=1.5)

# move cursor relative to current position of mouse
pyautogui.moveRel(20,0)

# it also has a duration to it
pyautogui.moveRel(200,0, duration = 2)

# to move up, the y coordinates are -ve going up
pyautogui.moveRel(0, -100)
# also pass the duration if you want
pyautogui.moveRel(0, -100, duration = 1)

# clicking on the help in vs code
# s1. Find the location where the mouse is placed
print(pyautogui.position())
# s2. use the click and make it click on the place you want(here on the help toolbar),
# if no arguments are passed, it clicks wherever the osition is immediately
pyautogui.click(480, 21)

# to double click use
pyautogui.doubleClick(480, 21)
# right click
pyautogui.rightClick(480, 21)
# middle button click
pyautogui.middleClick(480, 21)


# to figure out coordinates for every part that you might click on in the screen
# easier way is from terminal, and write the below two lines
import pyautogui
pyautogui.displayMousePosition() # shows the real time position of the mouse and the rgb values of pixel of the place your cursor is on