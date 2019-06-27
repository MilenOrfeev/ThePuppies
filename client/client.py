from tkinter import *
from PIL import ImageTk, Image
from HoverInfo import HoverInfo
from reviewMenu import ReviewMenu
from Dictionary import *


class Circle(Frame):
    def draw_circle(self, center_x, center_y, radius, colour=None):
        return self.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, activefill="grey", fill="red")
    Canvas.draw_circle = draw_circle


    def __init__(self, sid, x, y, radius, parent=None):
        Frame.__init__(self, parent)

        self.sid = sid
        self.hover = HoverInfo(self, 'kjsdfhkjsadh')
        self.x = x
        self.y = y
        self.radius = radius
        circle1 = canvas.draw_circle(x,y,radius)
        canvas.tag_bind(circle1,'<ButtonPress-1>',onObjectClick)


def onObjectClick(event):
    circleKey=event.widget.find_closest(event.x, event.y)[0]
    ReviewMenu(circleKey)


#This creates the main window of an application
window = Tk()
canvas = Canvas(window,width=640,height=449,bg="white")
canvas.grid()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
path = "office_layout.png"
img = ImageTk.PhotoImage(Image.open(path))
map = canvas.create_image(640, 200, image=img, anchor="e")
canvas.tag_lower(map)

for v in employeeDictionary.values():
    Circle(v['SID'],v['Coordinates'][0],v['Coordinates'][1],30)







#Start the GUI
window.mainloop()
