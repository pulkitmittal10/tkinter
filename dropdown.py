from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Drop_Down")
root.geometry("400x400")

options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

root.mainloop()