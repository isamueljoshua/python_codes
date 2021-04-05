# Tutorial below
# https://coderslegacy.com/python/python-gui/python-tkinter-button/

from tkinter import *

def set():
    print("HELLO World")

root = Tk()
root.geometry("200x150")
 
frame = Frame(root)
frame.pack()
button = Button(frame, text = "Button1", command = set,fg = "red", font = "Verdana 14 underline", bd = 2, bg = "light blue", relief = "groove")
button.pack()

root.mainloop()