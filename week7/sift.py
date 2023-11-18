import cv2
import numpy as np

img = cv2.imread('img1.jpg')
img = cv2.resize(img, (650, 600))
cv2.imshow('original', img)

g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift_ob = cv2.SIFT_create()
kp = sift_ob.detect(g, None)
img = cv2.drawKeypoints(g, kp, img)
img = cv2.resize(img, (650, 600))

cv2.imshow('sift', img)
cv2.waitKey(0)
cv2.destroyAllWindows()