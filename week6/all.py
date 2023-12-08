import cv2
from matplotlib import pyplot as plt

imgo = cv2.imread('img1.jpg')
img = cv2.cvtColor(imgo, cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(img, (3, 3), 0)

canny = cv2.Canny(img, 100, 200)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
# prewitt and robert include

images = [imgo, img, canny, laplacian, sobelx, sobely]
titles = ['original', 'grayscale', 'canny', 'laplacian', 'sobelx', 'sobely']

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], cmap='gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()