import cv2
import numpy as np

img1 = np.zeros((250,250,3),np.uint8)
img1 = cv2.rectangle(img1,(50,50),(300,100),(255,255,255),-1)
img2 = np.zeros((250,250,3),np.uint8)
img2 = cv2.circle(img2,(100,50),50,(255,255,255),-1)

#bitAnd = cv2.bitwise_and(img2,img1)
#bitOr = cv2.bitwise_or(img1,img2)
#bitXor = cv2.bitwise_xor(img1,img2)
bit_not = cv2.bitwise_not(img1)

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
#cv2.imshow('bitAnd',bitAnd)
#cv2.imshow('bitOr',bitOr)
#cv2.imshow('bitXor',bitXor)
cv2.imshow('bit_not',bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()