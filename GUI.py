import tkinter
from tkinter import messagebox
gui = tkinter.Tk()
def buttonRespond():
    messagebox.showinfo("message","Hello user")
    u = tkinter.Button(text= "fucking good isn't it??")
    u.pack()
b = tkinter.Button(text = "hello" , command  = buttonRespond)
b.pack()
gui.mainloop()
