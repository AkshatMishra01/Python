import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

img = Image.open('lena.jpg').convert('LA')
img.save('greyscale.jpg')

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

img = mpimg.imread('lena.jpg')

gray = rgb2gray(img)

plt.imshow(gray, cmap = plt.get_cmap('gray'))

plt.savefig('lena_greyscale.jpg')
plt.show()
