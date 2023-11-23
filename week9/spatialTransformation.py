import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('img2.jpg')

height, width = image.shape[:2]

angle = 45

scale_x = 1.5
scale_y = 1.5

tx = 50
ty = 50

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y)

translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, translation_matrix, (width, height))

images = [image, rotated_image, scaled_image, translated_image]
titles = ['Original Image', 'Rotated Image', 'Scaled Image', 'Translated Image']

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
