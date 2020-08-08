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






'''canvas '''
import tkinter
from tkinter import messagebox
gui = tkinter.Tk()
def buttonRespond():
    messagebox.showinfo("message","Hello user\ncanvas created")
    w = tkinter.Canvas(bg = "white",height = 250, width = 300)
    coord = 10,50,200,210
    arc = w.create_arc(coord, start = 0, extent = 180, fill = "green")
    w.pack()
    arc.pack()
b = tkinter.Button(text = "hello" ,activebackground = "red", font = "arial", command = buttonRespond)
b.pack()
gui.mainloop()
