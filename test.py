from tkinter import *        
from PIL import ImageTk, Image

app_root = Tk()

#Setting it up
img = ImageTk.PhotoImage(Image.open("test_image.jpg"))

#Displaying it
imglabel = Label(app_root, image=img).grid(row=1, column=1)        


app_root.mainloop()