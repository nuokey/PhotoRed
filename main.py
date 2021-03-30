from tkinter import *
from PIL import ImageTk, Image
from random import choice
from os import listdir

def open_file():
	global panel, img, img_panel, way
	images = []
	for i in listdir():
		q = i.split('.')
		if q[1] in ['png', 'jpg']:
			images.append(i)

	way = choice(images)
	img = Image.open(way)
	img_panel = ImageTk.PhotoImage(img)
	panel = Label(root, image = img_panel)
	panel.place(x = 60, y = 0)

def save_file():
	global img, way
	img.save(way)

def rotate_image():
	global panel, img, img_panel, way
	img = img.rotate(int(rotate_entry.get()))
	img_panel = ImageTk.PhotoImage(img)
	panel = Label(root, image = img_panel)
	panel.place(x = 60, y = 0)

root = Tk()

open_button = Button(root, text='Open', command=open_file)
open_button.place(x = 10, y = 10, width = 40)

save_button = Button(root, text='Save', command=save_file)
save_button.place(x = 10, y = 40, width = 40)

rotate_button = Button(root, text='Rotate', command=rotate_image)
rotate_button.place(x = 10, y = 70, width = 40)

rotate_entry = Entry(root)
rotate_entry.place(x = 10, y = 100, width = 40)

root.mainloop()