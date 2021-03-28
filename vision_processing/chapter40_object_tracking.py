import numpy as np
import cv2
cap = cv2.VideoCapture('highway.mp4')

ret,frame = cap.read()
x,y,width,height = 300,200,100,50
track_window = (x,y,width,height)
roi = frame[y:y+height,x:x+width]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi,np.array((0.,60.,32.)),np.array((180.,255.,255)))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
term_crit = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT,
             10,1)

cv2.imshow('roi',roi)
while True:
    ret,frame = cap.read()
    hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv_roi],[0],roi_hist,[0,180],1)
    ret,track_window = cv2.meanShift(dst,track_window,term_crit)
    x,y,w,h = track_window
    final_image = cv2.rectangle(frame,(x,y),(x+w,y+h),255,3)

    cv2.imshow('final',final_image)
    cv2.imshow('dst',dst)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
