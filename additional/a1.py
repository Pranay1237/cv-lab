import cv2
from matplotlib import pyplot as pp
import numpy as np

img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')
img3 = cv2.imread('img3.jpg')
img4 = cv2.imread('img4.jpg')
img5 = cv2.imread('img5.jpg')
img6 = cv2.imread('img6.jpg')

titles = ['img1', 'img2', 'img3', 'img4', 'img5', 'img6']
images = [img1, img2, img3, img4, img5, img6]

for i in range(6):
    pp.subplot(2, 3, i+1)
    pp.imshow(images[i])
    pp.title(titles[i])
    pp.xticks([])
    pp.yticks([])
pp.show()
# img = cv2.addWeighted(img2, 5.5, np.zeros(img2.shape, img2.dtype), 200, 300)
# cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()