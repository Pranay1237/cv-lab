import cv2
import numpy as np

image = cv2.imread('img1.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)

corners = np.float32(corners)

for corner in corners:
    x, y = corner[0]
    x = int(x)
    y = int(y)
    cv2.circle(image, (x, y), 6, (0, 255, 0), -1)

cv2.imshow('Shi-Tomasi Corner Detection', image)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.1, minDistance=20)

corners = np.float32(corners)

for corner in corners:
    x, y = corner[0]
    x = int(x)
    y = int(y)
    cv2.circle(image, (x, y), 6, (0, 255, 0), -1)

cv2.imshow('Shi-Tomasi', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
