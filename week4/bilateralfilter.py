import cv2, numpy as np, matplotlib.pyplot as plt

img=cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

kernel=np.ones((5 , 5), np.float32)/25

blurr=cv2.blur(img, (5 , 5) )
bilat=cv2.bilateralFilter(img,7,30,30)

titles=['image', 'blur image', 'bilteral image']
images=[img, blurr, bilat]

for i in range(3) :
     plt.subplot(1,3,i+1), plt.imshow(images[i],'gray')
     plt.title(titles[i])
     plt.xticks([ ]), plt.yticks([ ])
     
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()