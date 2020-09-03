from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap('C:/Users/Pulkit/Desktop/Programs/Python Projects/tkinter/file_icon.ico')

def popup():
	response = messagebox.askquestion("This is my Popup", "Hello World!")
	if response == "yes":
		Label(root, text="You Clicked Yes!").pack()
	else:
		Label(root, text="You Clicked No!").pack()

Button(root, text="Click Me!", command=popup).pack()

btn = Button(root, text="Open Second Window", command=lambda: new()).pack()

def new():
	global my_img
	top = Toplevel()
	Label(top, text="Hello World!").pack()
	my_img = ImageTk.PhotoImage(Image.open("images/Coffee.jpg"))
	my_label = Label(top, image=my_img).pack()

root.mainloop()