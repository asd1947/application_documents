import cv2
import numpy as np

cap = cv2.VideoCapture('lane_dection.mp4')
#rbg 9565
#def process(img):

def nothing(s):
    pass
cv2.namedWindow('tracking')
cv2.createTrackbar('mi','tracking',0,255,nothing)
cv2.createTrackbar('ma','tracking',0,255,nothing)

while(cap.isOpened()):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    mi = cv2.getTrackbarPos('mi','tracking')
    ma = cv2.getTrackbarPos('ma','tracking')
    _,th = cv2.threshold(img,225,255,cv2.THRESH_BINARY,3)
    #th = cv2.erode(th,(5,5),iterations=1)
    cv2.imshow('th', th)
    #frame = process(frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(40) == 27:
        break
cap.release()
cv2.destroyAllWindows()