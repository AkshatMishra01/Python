import tkinter 
from tkinter import messagebox
import webbrowser
import translate
import cv2
import requests
import  tqdm
import time 
def download(): 
    pass
def language():
    trans = translate.Translator(to_lang = 'Hindi')
    transitive = messagebox.showinfo('Messagebox',trans.translate('mood is high'))
    trans = tkinter.Toplevel(transitive)
def draw():
    c = tkinter.Toplevel(cursor = 'dot')
    c = tkinter.Canvas(width = 200, height = 200)
    c.pack()

def applications():
    url = 'https://Google.com'
    #webbrowser.register('chrome',None,webbrowser.BackgroundBrowser('C://Program Files (x86)//Google//chrome.exe'))
    webbrowser.open(url)
def multimedia():#######
    pass
gui = tkinter.Tk()
menubar = tkinter.Menu(gui)
filemenu = tkinter.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'Options',menu = filemenu)
filemenu.add_command(label = 'Download feature',command = download)#change
filemenu.add_command(label = 'language', command = language)# change
filemenu.add_command(label = 'monitor progress',  command = language) # change
filemenu.add_command(label = 'offline work', command =  language)# change
filemenu.add_separator()
filemenu.add_command(label ='exit  (to  exit the application)', command = menubar.quit)
homemenu1 = tkinter.Menu(menubar,tearoff = 0) 
sub = tkinter.Menu(homemenu1,tearoff = 0)
menubar.add_cascade(label = 'Home',menu = homemenu1)    
homemenu1.add_cascade(label = 'start',menu = sub)
sub.add_command(label = 'Canvas',command = draw)#changes
sub.add_command(label = 'entity calculator',command = language)#change
sub.add_command(label = 'hyertransmission', command = language)
apps = tkinter.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'Applications',menu = apps)
apps.add_command(label = 'Browser   (Default- Google Browser)',command =applications)
###apps.add_command(label = 'Multimedia',command = multimedia)
dsub = tkinter.Menu(download,tearoff = 0)
dsub.add_cascade(label = 'Modules',menu = download)
dsub.add_separator()
dsub.add_command(label = 'requirements have not been secified yet')
gui.config(menu = menubar)
gui.title('Backended gui using python')


gui.mainloop()
