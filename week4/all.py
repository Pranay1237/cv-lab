import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

kernel=np.ones((5 , 5), np.float32)/25

blurr=cv2.blur(img, (5 , 5) )
bilat=cv2.bilateralFilter(img,7,30,30)
gblur=cv2.GaussianBlur(img, (5 , 5), 0)
dst=cv2.filter2D(img,-1,kernel)
mdblur=cv2.medianBlur(img , 3)

titles=['image', 'blur image', 'bilteral image', '2D Convolution', 'gaussian blur', 'median blur']
images=[img, blurr, bilat, dst, gblur, mdblur]

for i in range(6) :
     plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
     plt.title(titles[i])
     plt.xticks([ ]), plt.yticks([ ])
     
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()