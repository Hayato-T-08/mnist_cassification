import tkinter
import os
from PIL import Image

class Scribble:
    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y, outline = "red", width = 5)
 
    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y, fill = "red", width = 5)
        self.sx = event.x
        self.sy = event.y
 
    def save_image(self, event):
        self.canvas.postscript(file='temp.ps',colormode='color')
        saving=Image.open('temp.ps')
        saving.save('temp.png')
        print("saved!")
 
    def __init__(self):
        window = tkinter.Tk()
        self.canvas = tkinter.Canvas(window, bg = "white", width = 300, height = 300)
        self.canvas.pack()
        quit_button = tkinter.Button(window, text = "Exit", command = window.quit)
        quit_button.pack(side = tkinter.RIGHT)
 
        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)
        self.canvas.bind("<ButtonPress-3>", self.save_image)
 
        window.mainloop()
 
Scribble()