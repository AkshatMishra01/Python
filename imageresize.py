import numpy as np
import cv2 
import face_recognition_models as fm

image = cv2.imread("C:\\a2.jpg",cv2.IMREAD_COLOR)
scale = 60  
width = int(image.shape[1] * scale / 100)  
height = int(image.shape[0] * scale / 100)  
dim = (width, height)  
# resize image  
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  
cv2.imshow("Resized image", resized)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
