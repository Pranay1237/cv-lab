import cv2, matplotlib.pyplot as plt

img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
val1, img1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
val2, img2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
val3, img3 = cv2.threshold(img, 150, 255, cv2.THRESH_TOZERO)
val4, img4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)

titles = ['original', 'thresh binary', 'thresh binary inverse', 'thresh tozero', 'thresh tozero inverse']
images = [img, img1, img2, img3, img4]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
