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
gui2.mainloop()

#new one
import tkinter 
from tkinter import messagebox
gui2 = tkinter.Tk()
frame = tkinter.Frame(gui2)
frame.pack()
command1 = bool
command2 = bool
var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
l = tkinter.Label(text = 'User Name')
e = tkinter.Entry(bd = 4,text ='left')
def function():
    messagebox.showinfo('GUI','select any one of the following')
b = tkinter.Button(text = "click me !", command = function)

def response():
    if command1 == True:
        messagebox.showinfo('please select a video from playlist')
    elif command2 == True:
        messagebox.showinfo('please select a song from playlist')

def video():
    messagebox.showinfo('GUI',"you selected video")
    c2.deselect()
    response()
    command1 = True
    return command1
def music():
    messagebox.showinfo('GUI','you selected music')
    c.deselect()
    command2 = True
    return command2
c = tkinter.Checkbutton(text = 'video',variable = var1,height = 5, width = 20,command = video)
c2 = tkinter.Checkbutton(text = 'music',variable = var2,height = 5, width = 20, command = music)
w1 = tkinter.Listbox()
w1.insert(1,'gui for access management')
w1.insert(2,'gui for seasonal projects')
w1.insert(3,'gui for selfmade antivirus')
w1.insert(4, ' website for gui construction')
w1.pack(side = 'top')
l.pack(side = 'left')
e.pack(side = 'left')
c.pack()
c2.pack()
b.pack(side = 'left')
gui2.mainloop()
