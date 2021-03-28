import numpy as np
import  cv2
img = cv2.imread('opencv-logo2.0.png')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imggray,254,255,0)
contours, heirachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Nunber of contour = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0), 3)

cv2.imshow('image',img)
cv2.imshow('image_gray',imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()

