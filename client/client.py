from tkinter import *
from PIL import ImageTk, Image
from reviewMenu import ReviewMenu
from Dictionary import *
from circle import Circle





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
    Circle(canvas,v['SID'],v['Coordinates'][0],v['Coordinates'][1],30)







#Start the GUI
window.mainloop()
