import cv2
import matplotlib.pyplot as plt

image = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)

images = [image, equalized_image]
titles = ['Original Image', 'Equalized Image']
# 4 images original image, equalized image, equalized histogram, CLAHE

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
