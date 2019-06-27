from tkinter import *
from PIL import ImageTk, Image
from HoverInfo import HoverInfo
from reviewMenu import ReviewMenu

class Example(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.l1 = Label(self, text="Hover over me")
        self.l2 = Label(self, text="", width=40)
        self.l1.pack(side="top")
        self.l2.pack(side="top", fill="x")

class Circle(Frame):
    def draw_circle(self, center_x, center_y, radius):
        return self.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, activefill="grey")
    Canvas.draw_circle = draw_circle

    def __init__(self, sid, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        self.sid = sid
        self.lbl = Label(self, text='testing')
        self.lbl.grid()
        self.hover = HoverInfo(self, 'kjsdfhkjsadh')
        circle1 = canvas.draw_circle(100, 120, 10)
        canvas.tag_bind(circle1,'<ButtonPress-1>',onObjectClick(sid))



def onObjectClick(sid):
    ReviewMenu(sid)


#This creates the main window of an application
window = Tk()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
path = "office_layout.png"
img = ImageTk.PhotoImage(Image.open(path))



canvas = Canvas(window,width=640,height=449,bg="white")
canvas.grid()
map = canvas.create_image(640, 200, image=img, anchor="e")
canvas.tag_lower(map)


circle = Circle("A11111")





#Start the GUI
window.mainloop()
