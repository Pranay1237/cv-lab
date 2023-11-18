import cv2

img1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
_ , baw = cv2.threshold(img1, 128, 255, cv2.THRESH_BINARY)

cv2.imshow('img1', img1)
cv2.imshow('img2', baw)
cv2.waitKey(0)
cv2.destroyAllWindows()