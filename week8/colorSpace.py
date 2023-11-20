import cv2
import numpy as np

# Load the RGB image
image = cv2.imread('img1.jpg')

# Convert RGB to CMY
cmy_image = 255 - image
cmy = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Convert RGB to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display the converted images
cv2.imshow('CMY Image', cmy_image)
cv2.imshow('CMY', cmy)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
