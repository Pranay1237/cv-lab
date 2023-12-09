import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('flower.jpg')

bnw = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE)
cmy_image = 255 - image
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

images = [image, bnw, cmy_image, lab, hsv_image, hls_image]
titles = ['Original Image', 'GrayScale', 'CMY Image', 'LAB', 'HSV Image', 'HLS Image']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()