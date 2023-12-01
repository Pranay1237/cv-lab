import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('shapes.jpg')
img = cv2.resize(img, (650, 600))
img1 = img.copy()

g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift_ob = cv2.SIFT_create()
kp = sift_ob.detect(g, None)
img = cv2.drawKeypoints(g, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img = cv2.resize(img, (650, 600))

images = [img1, img]
titles = ['Original Image', 'SIFT Image']

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()