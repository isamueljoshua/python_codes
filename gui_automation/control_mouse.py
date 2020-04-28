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

