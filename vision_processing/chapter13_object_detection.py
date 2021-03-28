import cv2
import numpy as np
def nothing(s):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('tracking')

cv2.createTrackbar('lh','tracking',0,255,nothing)
cv2.createTrackbar('uh','tracking',0,255,nothing)
cv2.createTrackbar('ls','tracking',0,255,nothing)
cv2.createTrackbar('us','tracking',0,255,nothing)
cv2.createTrackbar('lv','tracking',0,255,nothing)
cv2.createTrackbar('uv','tracking',0,255,nothing)

while 1:
    #frame = cv2.imread('smarties.png')
    x,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('lh', 'tracking')
    uh = cv2.getTrackbarPos('uh', 'tracking')
    ls = cv2.getTrackbarPos('ls', 'tracking')
    us = cv2.getTrackbarPos('us', 'tracking')
    lv = cv2.getTrackbarPos('lv', 'tracking')
    uv = cv2.getTrackbarPos('uv', 'tracking')

    lb = np.array([lh,ls,lv])
    ub = np.array([uh,us,uv])

    mask = cv2.inRange(hsv,lb,ub)

    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()