import tkinter as tk
from tkinter.constants import LEFT 
import cv2 
import datetime as dt

def resize():
    pass

def gray_scale():
    pass

def video_capture():
    cap = cv2.VideoCapture(0)
    success, img = cap.read()
    while True:
        cv2.imshow("Live cam",img)
        cv2.waitKey(1)

top = tk.Tk()
w = tk.Button(top, text= 'Video_Capture', command=video_capture)
x = tk.Button(top, text= "Gray-Scaler", command=gray_scale)
y = tk.Button(top, text= "resize", command=resize)
w.pack()
x.pack()
top.mainloop()
