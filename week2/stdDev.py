import cv2

image = cv2.imread('img1.jpg')

mean, stddev = cv2.meanStdDev(image)

print("standard deviation : ", stddev)