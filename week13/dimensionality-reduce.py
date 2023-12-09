import cv2
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('flower.jpg', cv2.IMREAD_GRAYSCALE)

# Flatten the image to a 1D array
img_flattened = img.flatten()

# Apply PCA
pca = PCA(n_components=0.95)  # You can adjust the explained variance threshold
img_pca = pca.fit_transform(img_flattened.reshape(1, -1))

# Inverse transform to get the reduced image
img_reduced = pca.inverse_transform(img_pca)

# Reshape the flattened image to its original shape
img_reduced = img_reduced.reshape(img.shape)

# Display the original and reduced images
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(img_reduced, cmap='gray')
plt.title('Reduced Dimensionality using PCA')

plt.show()
