from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from random import choice
from os import listdir

def open_file():
	global panel, img, img_panel, way
	images = []
	print(listdir())
	for i in listdir():
		q = i.split('.')

		if q[1] in ['png', 'jpg']:
			images.append(i)

	way = choice(images)
	img = Image.open(way)
	update_image(img)

def save_file():
	global img, way
	img.save(way)

def update_image(new_img):
	global img_panel, panel, img
	img = new_img.resize((int(new_img.size[0] * (720 / new_img.size[1])), 720))
	img_panel = ImageTk.PhotoImage(img)
	panel = Label(root, image = img_panel)
	panel.place(x = 60, y = 0)

def rotate_image():
	global img
	img = img.rotate(int(rotate_entry.get()))
	update_image(img)

def crop_image():
	global img
	crop_size = (crop_entry.get()).split(' ')
	img = img.crop((int(crop_size[0]), int(crop_size[1]), int(crop_size[2]), int(crop_size[3])))
	update_image(img)

def blur_image():
	global img
	img = img.filter(ImageFilter.BLUR)
	update_image(img)

def sharpen_image():
	global img
	img = img.filter(ImageFilter.SHARPEN)
	update_image(img)

def emboss_image():
	global img
	img = img.filter(ImageFilter.EMBOSS)
	update_image(img)

def detail_image():
	global img
	img = img.filter(ImageFilter.DETAIL)
	update_image(img)

def smooth_image():
	global img
	img = img.filter(ImageFilter.SMOOTH)
	update_image(img)

def contour_image():
	global img
	img = img.filter(ImageFilter.CONTOUR)
	update_image(img)

def blue_image():
	global img
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			rgb = img.getpixel((x, y))
			blue = 255
			img.putpixel((x, y), (rgb[0], rgb[1], blue))

	update_image(img)

def red_image():
	global img
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			rgb = img.getpixel((x, y))
			red = 255
			img.putpixel((x, y), (red, rgb[1], rgb[2]))

	update_image(img)

def green_image():
	global img
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			rgb = img.getpixel((x, y))
			green = 255
			img.putpixel((x, y), (rgb[0], green, rgb[2]))

	update_image(img)



root = Tk()
root.geometry("1280x720")

open_button = Button(root, text='Open', command=open_file)
open_button.place(x = 5, y = 10, width = 50)

save_button = Button(root, text='Save', command=save_file)
save_button.place(x = 5, y = 40, width = 50)

rotate_button = Button(root, text='Rotate', command=rotate_image)
rotate_button.place(x = 5, y = 70, width = 50)

rotate_entry = Entry(root)
rotate_entry.place(x = 5, y = 100, width = 50)

crop_button = Button(root, text='Crop', command=crop_image)
crop_button.place(x = 5, y = 130, width = 50)

crop_entry = Entry(root)
crop_entry.place(x = 5, y = 160, width = 50)

blur_button = Button(root, text='Blur', command=blur_image)
blur_button.place(x = 5, y = 190, width = 50)

sharpen_image = Button(root, text='Sharpen', command=sharpen_image)
sharpen_image.place(x = 5, y = 220, width = 50)

emboss_image = Button(root, text='Emboss', command=emboss_image)
emboss_image.place(x = 5, y = 250, width = 50)

blue_button = Button(root, text='Blue', command=blue_image)
blue_button.place(x = 5, y = 280, width = 50)

red_button = Button(root, text='Red', command=red_image)
red_button.place(x = 5, y = 310, width = 50)

green_button = Button(root, text='Green', command=green_image)
green_button.place(x = 5, y = 340, width = 50)

detail_button = Button(root, text='Detail', command=detail_image)
detail_button.place(x = 5, y = 370, width = 50)

smooth_button = Button(root, text='Smooth', command=smooth_image)
smooth_button.place(x = 5, y = 400, width = 50)

contour_button = Button(root, text='Contour', command=contour_image)
contour_button.place(x = 5, y = 430, width = 50)

root.mainloop()