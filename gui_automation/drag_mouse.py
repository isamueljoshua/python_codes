import pyautogui

pyautogui.click() # click to put paint in focus
distance = 200

while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration = 0.1) # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration = 0.1) # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration = 0.1) # move left
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration = 0.1) # move up


'''
What to do in case your pyautogui pgm is executing continuously without your control
Just Move the mouse to top left corner (0,0) and then leave it there for a few seconds, so the program stops now
Pyautogui programs by default has a 10th of a second delay after every single call
This is a failsafe exception that pyautogui has inbuilt in the library
'''