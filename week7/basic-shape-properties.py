import cv2

img = cv2.imread('img6.jpg')
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

cv2.imshow('original', img)
print('dimensions: ', dimensions)
print('height: ', height)
print('width: ', width)
print('number of channels: ', channels)

cv2.waitKey(0)
cv2.destroyAllWindows()