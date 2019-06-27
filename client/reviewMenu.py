from tkinter import *
from PIL import ImageTk, Image
class ReportMenu(Menu):
    def callback(self):
        print("hello")

    def __init__(self,name):
        window = Tk()

        #frame = Frame(window, width=400, height=400, bg = 'red')
        #frame.grid(row=0)
        l1 = Label(window,text="You have succesfully reported "+str(name)+".\n Building Mngmt. has been informed  and will be there shortly.")
        l1.pack(anchor='center')
        mainloop()

class EditMenu(Menu):
    def callback(self):
        print("hello")

    def __init__(self):
        window = Tk()

        # frame = Frame(window, width=400, height=400, bg = 'red')
        # frame.grid(row=0)
        l1 = Label(window,
                   text="employee removed from chair")
        l1.pack(anchor='center')
        mainloop()

class ReviewMenu(Menu):

    def callback(self):
        print("hello")


    def __init__(self,personProfile):
        self.personProfile = personProfile
        window = Tk()
        self.Name = personProfile['Name']
        self.Role = personProfile['Role']
        self.Team = personProfile['Team']
        frame = Frame(window, width= 200, height = 400)
        l1 = Label(frame, text="Name:  " + str(self.Name))
        l1.pack()
        l2 = Label(frame, text="Position:  " + str(self.Role))
        l2.pack()
        l3 = Label(frame, text="Team:  " + str(self.Team))
        l3.pack()
        #l2 = Text(frame, text="Name:  " + str(self.Name), height=40, width=200)

        frame.grid(row = 0)
        def callback():
            EditMenu()
        def callback2():
            ReportMenu(self.Name)
            # form to edit
        EDIT = Button(window, text = "Remove "+ str(self.Name) +" from Chair", command=callback)
        REPORT = Button(window, bg = 'red', fg = 'red', text="REPORT!!!!!", command=callback2)
        EDIT.grid(row = 1, column = 0)
        REPORT.grid(row = 1, column = 1)

        mainloop()
