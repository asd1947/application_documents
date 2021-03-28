import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi.jpg',0)

def nothing(x):
    print(x)

cv2.namedWindow('th')

cv2.createTrackbar('th1','th',0,255,nothing)
cv2.createTrackbar('th2','th',0,255,nothing)

while 1:
    th1 = cv2.getTrackbarPos('th1', 'th')
    th2 = cv2.getTrackbarPos('th2', 'th')

    canny = cv2.Canny(img,th1,th2)

    cv2.imshow('image',img)
    cv2.imshow('canny',canny)

    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()