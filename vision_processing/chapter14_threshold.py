import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('gradient.png',0)
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,50,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,50,255,cv2.THRESH_TOZERO_INV)

titles = ['original_image','binary','binary_inv','trunc','tozero','tozero_inv']
image = [img,th1,th2,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(image[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

"""cv2.imshow('image',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)
cv2.imshow('th5',th5)

cv2.waitKey(0)
cv2.destroyAllWindows()"""
plt.show()
