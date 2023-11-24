import cv2
import numpy as np

image = cv2.imread('img2.jpg')
cv2.imshow('Original Image', image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)[1]

dst = cv2.dilate(dst, None)

image[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('Corner Harris', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
