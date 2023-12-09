import cv2
import matplotlib.pyplot as plt

image = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)

equalized_image = cv2.equalizeHist(image)

# Calculate histograms
hist_image = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_equalized_image = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

images = [image, hist_image, equalized_image, hist_equalized_image]
titles = ['Original Image', 'Original Histogram', 'Equalized Image', 'Equalized Histogram']

# Plot images and histograms
plt.figure(figsize=(10, 5))

for i in range(4):
    if i%2 == 0:
        plt.subplot(2, 2, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    else:
        plt.subplot(2, 2, i+1)
        plt.plot(images[i])
        plt.title(titles[i])
        plt.xlim([0, 256])

plt.show()
