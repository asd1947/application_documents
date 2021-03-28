import numpy as np
import cv2

img = cv2.imread('shape.png')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(imggray,240,255,cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(img,[approx],0,(0,0,0),1)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img,'triangle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    elif len(approx) == 4:
        x1,y1,w,h = cv2.boundingRect(approx)
        aspectratio = float(w)/h
        print(aspectratio)
        if aspectratio >= 0.95 and aspectratio <= 1.05:
            cv2.putText(img,'square',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
        else:
            cv2.putText(img,'rectangle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    elif len(approx) == 5:
        cv2.putText(img,'pentagon',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    else:
        cv2.putText(img,'circle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))

cv2.imshow('shape',img)
cv2.waitKey(0)
cv2.destroyAllWindows()