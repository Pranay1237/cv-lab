import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img, (3, 3), 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('laplacian'), plt.xticks([]), plt.yticks([])
plt.show()