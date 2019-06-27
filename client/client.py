from tkinter import *
from PIL import ImageTk, Image
import re
from HoverInfo import HoverInfo
from reviewMenu import ReviewMenu

class Circle(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        self.lbl = Label(self, text='testing')
        self.lbl.grid()
        self.hover = HoverInfo(self, 'kjsdfhkjsadh')
        circle1 = canvas.create_oval(100,100,90,90)
        canvas.tag_bind(circle1,'<ButtonPress-1>',onObjectClick)



def onObjectClick(event):
    print()
    ReviewMenu()

#This creates the main window of an application
window = Tk()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
path = "office_layout.png"
img = ImageTk.PhotoImage(Image.open(path))



canvas = Canvas(window,width=640,height=449,bg="white")
canvas.grid()
map = canvas.create_image(640, 200, image=img, anchor="e")
canvas.tag_lower(map)

circle = Circle()







#Start the GUI
window.mainloop()
