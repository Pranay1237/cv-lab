import cv2, numpy as np, matplotlib.pyplot as plt

img=cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

kernel=np.ones((5 , 5), np.float32)/25

dst=cv2.filter2D(img,-1,kernel)

titles=['image','2D Convolution']
images=[img,dst]

for i in range(2) :
     plt.subplot(2,2,i+1), plt.imshow(images[i],'gray')
     plt.title(titles[i])
     plt.xticks([ ]), plt.yticks([ ])
     
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()