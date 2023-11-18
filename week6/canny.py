import cv2

img = cv2.imread('img6.jpg')
edge = cv2.Canny(img, 100, 200)
edge1 = cv2.Canny(img, 100, 200, apertureSize=5)

cv2.imshow('original', img)
cv2.imshow('edge', edge)
cv2.imshow('edge1', edge1)

cv2.waitKey(0)
cv2.destroyAllWindows()