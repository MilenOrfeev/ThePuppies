import tkinter as tk
from PIL import ImageTk, Image

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.l1 = tk.Label(self, text="Hover over me")
        self.l2 = tk.Label(self, text="", width=40)
        self.l1.pack(side="top")
        self.l2.pack(side="top", fill="x")

        self.l1.bind("<Enter>", self.on_enter)
        self.l1.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.l2.configure(text="Hello world")

    def on_leave(self, enter):
        self.l2.configure(text="")


#This creates the main window of an application
window = tk.Tk()

path = "office_layout.png"
img = ImageTk.PhotoImage(Image.open(path))


canvas = tk.Canvas(window,width=640,height=449,bg="white")
canvas.grid()
map = canvas.create_image(640, 200, image=img, anchor="e")
canvas.tag_lower(map)

circle1 = canvas.create_oval(100,100,90,90)

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.

#The Pack geometry manager packs widgets in rows or columns.


#Start the GUI
# Example(window).pack(side="top", fill="both", expand="true")
window.mainloop()
