import numpy as np
import cv2

img = cv2.imread('messi.jpg')
logo = cv2.imread('opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340,330:390]
#cv2.imshow('ball',ball)
img[273:333,100:160] = ball

img = cv2.resize(img,(512,512))
logo = cv2.resize(logo,(512,512))
#dst = cv2.add(img,logo)

dst = cv2.addWeighted(img,.7,logo,.3,0)

#cv2.imshow('image',img)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()