# Tutorial below
# https://coderslegacy.com/python/python-gui/python-tkinter-frame/

from tkinter import *


"""
Using pack() instead of other placement functions like place() allows the frames and their contents to auto adjust as window size is adjusted. 
pack() can also take several parameters to adjust position of the widget.
"""
root = Tk()
# way of setting the size for the whole window.
root.geometry("200x150")
frame = Frame(root, bd = 5, bg = "purple")
frame.pack()

leftframe = Frame(root, bg = "blue", bd = 3)
leftframe.pack(side=LEFT)

rightframe = Frame(root, bg = "red", bd = 3)
rightframe.pack(side=RIGHT)

label = Label(frame, text = "Hello world")
label.pack()

button1 = Button(leftframe, text = "Button1")
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "Button2")
button2.pack(padx = 3, pady = 3)
button3 = Button(leftframe, text = "Button3")
button3.pack(padx = 3, pady = 3)

#  add a title on the title bar of the window.
root.title("Test")
# triggers the GUI. Any modifications and widgets to be included should be written before it.
root.mainloop()