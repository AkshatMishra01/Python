import cv2
# Here, let's start by importing a picture into our this program
x = cv2.imread("C:/a.jpg",cv2.IMREAD_COLOR)
cv2.imshow("A1",x)
cv2.waitKey(0)
cv2.destroyAllWindows()
