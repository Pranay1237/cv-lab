import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('img2.jpg')

cmy_image = 255 - image
cmy = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

images = [image, cmy_image, cmy, hsv_image]
titles = ['Original Image', 'CMY Image', 'CMY', 'HSV Image']

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()