import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

_ , img1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

dialate = cv2.dilate(img1, kernel, iterations=2)
erode = cv2.erode(img1, kernel, iterations=2)
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)
mg = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)
th = cv2.morphologyEx(img1, cv2.MORPH_TOPHAT, kernel)

titles = ['original', 'binary', 'dialate', 'erode', 'opening', 'closing', 'gradient', 'tophat']
images = [img, img1, dialate, erode, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()