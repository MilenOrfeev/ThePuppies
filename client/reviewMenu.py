from tkinter import *
from PIL import ImageTk, Image
#from editForm import EditForm

class ReviewMenu(Menu):

    def callback(self):
        print("hello")


    def __init__(self,circleKey):
        self.circleKey = circleKey
        window = Tk()

        frame = Frame(window, width= 200, height = 400)
        frame.grid(row = 0)

        def callback():
            # form to edit
            EditForm();
        a = Button(window, text = "edit employee", command=callback)
        REPORT = Button(window, bg = 'red', fg = 'red', text="REPORT!!!!!", command=callback)
        a.grid(row = 1, column = 0)
        REPORT.grid(row = 1, column = 1)

        mainloop()
