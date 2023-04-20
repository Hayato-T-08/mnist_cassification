import tkinter
import os
from PIL import Image,ImageOps
import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10,activation='softmax')
])

model.load_weights('mnist_weight.hdf5')

class Scribble:
    def on_pressed(self, event):
        self.sx = event.x
        self.sy = event.y
        self.canvas.create_oval(self.sx, self.sy, event.x, event.y,
                                outline = self.color.get(),
                                width = 15)


    def on_dragged(self, event):
        self.canvas.create_line(self.sx, self.sy, event.x, event.y,
                            fill = self.color.get(),
                            width = 15)
        self.sx = event.x
        self.sy = event.y

    
    def change_mode(self):
        
        if self.write_button['state'] == tkinter.NORMAL:
            self.write_button['state'] = tkinter.DISABLED
            self.erase_button['state'] = tkinter.NORMAL
            self.color.set("black") 

           
        else:
            
            self.write_button['state'] = tkinter.NORMAL
            self.erase_button['state'] = tkinter.DISABLED
            self.color.set('white')
 
    def save_image(self):
        self.canvas.postscript(file='temp.ps',colormode='color')
        saving=Image.open('temp.ps')
        saving.save('temp.png')
        im=Image.open('temp.png').convert('RGB')
        im_invert = ImageOps.invert(im)
        im_invert.save('temp.png')
        print("saved!")
        img=Image.open(f'temp.png').convert('L')
        img_resize=img.resize((28,28))
        img_array=np.array(img_resize)
        imgs=img_array[np.newaxis,:,:]

        pred = model.predict(imgs)

        classification=np.argmax(pred)
        print(classification)
        self.text=tkinter.Label(text="You wrote {}".format(classification))
        self.text.pack()

    
    def reset_canvas(self):
        self.canvas.delete("all")
        self.text.pack_forget()

    def __init__(self):
        window = tkinter.Tk()
        window.title("mnist classification")
        self.canvas = tkinter.Canvas(window, bg = "white", width = 300, height = 300)
        self.canvas.pack()
        
        self.introducion=tkinter.Label(window,text='Please write the numbers 0 to 9.')
        self.introducion.pack()

        self.text=None

        self.color = tkinter.StringVar()                    
        self.color.set("black") 

        self.canvas.bind("<ButtonPress-1>", self.on_pressed)
        self.canvas.bind("<B1-Motion>", self.on_dragged)

        self.write_button=tkinter.Button(window,text="write",command=self.change_mode)
        self.write_button.pack(side=tkinter.LEFT)

        self.erase_button=tkinter.Button(window,text="eraser",command=self.change_mode)
        self.erase_button.pack(side=tkinter.LEFT)
        self.rest_button=tkinter.Button(window,text="reset",command=self.reset_canvas)
        self.rest_button.pack(side=tkinter.LEFT)

        self.save_button=tkinter.Button(window,text="submit",command=self.save_image)
        self.save_button.pack(side=tkinter.LEFT)

        self.quit_button = tkinter.Button(window, text = "exit", command = window.quit)
        self.quit_button.pack(side = tkinter.LEFT)
 
        window.mainloop()
 
Scribble()