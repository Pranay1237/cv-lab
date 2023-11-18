import cv2
import numpy as np

image = cv2.imread('img1.jpg')

mean = cv2.mean(image)
print(mean)