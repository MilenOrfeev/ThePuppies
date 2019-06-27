from tkinter import *


class EditForm():

    def callback(self):
        print("hello")


    def __init__(self):
        window = Tk()

        frame = Frame(window, width= 200, height = 400)
        frame.grid(row = 0)
        def callback():
            print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE");
            # form to edit
            editForm();
        a = Button(window, text = "edit", command=callback)

        a.grid(row = 1)

        mainloop()
