import cv2
import numpy as np

image = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

minv, maxv, minl, maxl = cv2.minMaxLoc(image)

print("minimum value : ", minv)
print("maximum value : ", maxv)
print("minimum location : ", minl)
print("maximum location : ", maxl)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()