from tkinter import *


class ReviewMenu(Menu):
    def __init__(self,sid):
        window = Tk()
        canvas = Canvas(window,width=300,height=400,bg="white")
        canvas.grid()
        print(sid)
