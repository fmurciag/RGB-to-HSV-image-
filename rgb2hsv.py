import cv2

# Load an image
imgName='pargo.jpg'
img = cv2.imread(imgName)

#convert RGB to HSV (0-360)
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)

#save the image
cv2.imwrite('hsv_'+imgName,img)