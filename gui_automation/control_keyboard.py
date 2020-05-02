import pyautogui
# to write anything to the interface, first open notepad, click on the position where you want to write then write
# to do this in a single line
pyautogui.click(100, 100);pyautogui.typewrite('Hello world!')
pyautogui.click(100, 100);pyautogui.typewrite('Hello world!', interval=0.2)

# to use keys, just pass it a list of keys to press
# so below code presses the a key, b key, then left button, left again, then caps X and Y
pyautogui.click(100, 100);pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)

# PRINTS ALL THE AVAILABLE KEYBOARD KEYS
print(pyautogui.KEYBOARD_KEYS)

# to press just one key
# pressing the F5 key here for example
pyautogui.press('f5')

# to open multiple keys in combination
pyautogui.click(100, 100);pyautogui.hotkey('ctrl', 'o')