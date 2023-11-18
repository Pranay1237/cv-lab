import cv2

img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

val, imgt = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('img', img)
cv2.imshow('imgt', imgt)
cv2.waitKey(0)
cv2.destroyAllWindows()
