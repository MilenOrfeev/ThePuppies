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

class EditMenu(Menu):
    def callback(self):
        print("hello")

    def __init__(self):
        window = Tk()
        window.title("Edit Employee Information")
        window.geometry('400x400')
        window.configure(b=1)
        c1 = Entry(window).grid(row=2, column=1)
        d1 = Entry(window).grid(row=3, column=1)

        def clicked():
            res = "Welcome to " + txt.get()
            lbl.configure(text=res)

        btn = Button(window, text="Submit").grid(row=4, column=0)
        window.mainloop()
        mainloop()ackground="grey");
        firstName = Label(window, text="First Name").grid(row=0, column=0)
        lastName = Label(window, text="Last Name").grid(row=1, column=0)
        seatID = Label(window, text="Seat ID").grid(row=2, column=0)
        jobRole = Label(window, text="Job Role").grid(row=3, column=0)
        a1 = Entry(window).grid(row=0, column=1)
        b1 = Entry(window).grid(row=1, column=1)
        c1 = Entry(window).grid(row=2, column=1)
        d1 = Entry(window).grid(row=3, column=1)

        def clicked():
            res = "Welcome to " + txt.get()
            lbl.configure(text=res)

        btn = Button(window, text="Submit").grid(row=4, column=0)
        window.mainloop()
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
            EditMenu()
        def callback2():
            ReportMenu()
            # form to edit
        EDIT = Button(window, text = "edit employee", command=callback)
        REPORT = Button(window, bg = 'red', fg = 'red', text="REPORT!!!!!", command=callback2)
        EDIT.grid(row = 1, column = 0)
        REPORT.grid(row = 1, column = 1)

        mainloop()
