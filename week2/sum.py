import cv2
import numpy as np

matrix = cv2.imread('img1.jpg')

sum_result = cv2.sumElems(matrix)

print("sum of elements : ", sum_result)