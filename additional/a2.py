from PIL import Image, ImageEnhance
from matplotlib import pyplot as pp
import cv2

img = Image.open('img1.jpg')
#im3 = ImageEnhance.Sharpness(img)
#im3 = ImageEnhance.Brightness(img)
im3 = ImageEnhance.Color(img)

images = []
titles = []

for i in range(1, 7):
    images.append(im3.enhance(i*1.2))
    titles.append(str(i*1.2))


for i in range(6):
    pp.subplot(2, 3, i+1)
    pp.imshow(images[i], 'gray')
    pp.title(titles[i])
    pp.xticks([]),pp.yticks([])

pp.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
    