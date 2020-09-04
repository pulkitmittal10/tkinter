from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("File Viewer")

def open():
	global my_img
	root.filename = filedialog.askopenfilename(initialdir="C:/Users/Pulkit/Desktop/Programs/Python Projects/tkinter/images", title="Select a file:",filetypes=(("jpg files","*.jpg"), ("all files","*.*"), ("png files","*.png")))
	my_label = Label(root, text=root.filename).pack()

	my_img = ImageTk.PhotoImage(Image.open(root.filename))
	my_image_label = Label(root, image=my_img).pack()


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()