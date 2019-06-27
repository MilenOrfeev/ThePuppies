from tkinter import *


class ReviewMenu(Menu):

    def callback(self):
        print("hello")


    def __init__(self):
        window = Tk()

        frame = Frame(window, width= 200, height = 400)
        frame.grid(row = 1)
        a = Button(window, text = "edit")

        a.grid(row = 0)

        mainloop()
