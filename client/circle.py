from tkinter import *
from reviewMenu import ReviewMenu

class Circle(Frame):

    
    def draw_circle(self, center_x, center_y, radius):
        return self.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, activefill="grey")
    Canvas.draw_circle = draw_circle


    def __init__(self, canvas, sid, x, y, radius, parent=None):
        def onObjectClick(event):
            circleKey=event.widget.find_closest(event.x, event.y)[0]
            ReviewMenu(circleKey)
        Frame.__init__(self, parent)

        self.sid = sid
        self.x = x
        self.y = y
        self.radius = radius
        circle1 = canvas.draw_circle(x,y,radius)
        canvas.tag_bind(circle1,'<ButtonPress-1>',onObjectClick)
