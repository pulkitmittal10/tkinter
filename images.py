from tkinter import *

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap('C:/Users/Pulkit/Desktop/Programs/Python Projects/tkinter/file_icon.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()



root.mainloop()