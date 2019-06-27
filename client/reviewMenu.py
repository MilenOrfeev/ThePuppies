from tkinter import *


class ReviewMenu(Menu):
    def __init__(self,circleKey):
        self.circleKey = circleKey
        window = Tk()
        canvas = Canvas(window,width=300,height=400,bg="white")
        canvas.grid()

        print (circleKey)
