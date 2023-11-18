import cv2
from matplotlib import pyplot as plt

img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

img = cv2.GaussianBlur(img, (3, 3), 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobelxy = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(sobelx, cmap='gray')
plt.title('sobelx'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobely, cmap='gray')
plt.title('sobely'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobelxy, cmap='gray')
plt.title('sobelxy'), plt.xticks([]), plt.yticks([])

plt.show()
