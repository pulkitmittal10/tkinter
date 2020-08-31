from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap('C:/Users/Pulkit/Desktop/Programs/Python Projects/tkinter/file_icon.ico')

# r = IntVar()

toppings=[
	("Pepperoni","Pepperoni"),
	("Cheese","Cheese"),
	("Mushroom","Mushroom"),
	("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

def clicked(value):
	mylabel = Label(root, text=value)
	mylabel.pack()	

for text, mode in toppings:
	Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# mylabel = Label(root, text=pizza.get())
# mylabel.pack()	

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()