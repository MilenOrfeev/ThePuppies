from tkinter import *
from PIL import ImageTk, Image
class ReportMenu(Menu):
    def callback(self):
        print("hello")

    def __init__(self):
        window = Tk()

        #frame = Frame(window, width=400, height=400, bg = 'red')
        #frame.grid(row=0)
        l1 = Label(window,text="You have succesfully reported the desk.\n Building Mngmt. has been informed  and will be there shortly.")
        l1.pack(anchor='center')
        mainloop()

class ReviewMenu(Menu):

    def callback(self):
        print("hello")


    def __init__(self,circleKey):
        self.circleKey = circleKey
        window = Tk()

        frame = Frame(window, width= 200, height = 400)
        frame.grid(row = 0)
        def callback():
            print("a")
        def callback2():
            ReportMenu()
            # form to edit
        a = Button(window, text = "edit employee", command=callback)
        REPORT = Button(window, bg = 'red', fg = 'red', text="REPORT!!!!!", command=callback2)
        a.grid(row = 1, column = 0)
        REPORT.grid(row = 1, column = 1)

        mainloop()
