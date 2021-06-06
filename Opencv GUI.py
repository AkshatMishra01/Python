import tkinter as tk
from tkinter.constants import LEFT 
import numpy as np 
import cv2 
import datetime as dt

kernel = np.ones((5,5),np.uint8)
def resize():
    path = input("Enter the image path, in the path box:")
    img = cv2.imread(path,cv2.IMREAD_COLOR)
    height = input("Desired Height:")
    width = input("Desired width:")
    cv2.resize(img)

def eroder():
    path = input("enter the path for the image")
    img = cv2.imread(path,cv2.IMREAD_COLOR)
    imgerode = cv2.erode(img,kernel,iterations=1)
    cv2.imshow("Eroded image", imgerode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def blur():
    path = input("Enter the image path")
    img = cv2.imread(path,cv2.IMREAD_COLOR)
    imgblur = cv2.GaussianBlur(img,(7,7),0)
    cv2.imshow("Blurred image",imgblur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def gray_scaler():
    path = input("Enter the image path, in the path box:")
    img = cv2.imread(path,cv2.COLOR_RGB2GRAY)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def video_capture():
    cap = cv2.VideoCapture(0)
    cap.set(10,50)
    while True:
        success, img = cap.read()
        cv2.imshow("Live cam",img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break

def canny():
    path = input("Enter the image path,in the path box:")
    img = cv2.imread(path,cv2.IMREAD_COLOR)
    imgcanny = cv2.Canny(img,150,200)
    cv2.imshow("Canny",imgcanny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save():
    pass

def dialator():
    path = input("Enter the image path, in the path box:")
    img = cv2.imread(path,cv2.IMREAD_COLOR)
    imgdialated = cv2.dilate(img, kernel,iterations=1)
    cv2.imshow("Dialeted Image",imgdialated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

top = tk.Tk()
w = tk.Button(top, text= 'Video_Capture', command=video_capture)
x = tk.Button(top, text= "Gray-Scaler", command=gray_scaler)
y = tk.Button(top, text= "resize", command=resize)
z = tk.Button(top, text= "Blur", command=blur)
u = tk.Button(top, text="Edge_detector",command=canny)
d = tk.Button(top, text= "Dialator", command=dialator)
e = tk.Button(top, text="Eroder image" ,command=eroder)

e.pack()
d.pack()
u.pack()
w.pack()
x.pack()
y.pack()
z.pack()
top.mainloop()
