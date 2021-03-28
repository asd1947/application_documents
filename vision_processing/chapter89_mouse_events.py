import numpy as np
import cv2


#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)
""""#lesson8
def click_event(event, x, y,flage,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x)+', '+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,255,0),2)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR= str(blue) + ', '+ str(green)+', '+ str(red)
        print(strBGR)
        cv2.putText(img,strBGR,(x,y),font,1,(200,0,200),2)
        cv2.imshow('image',img)"""

#lesson9
def click_event(event,x,y,flage,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255,0,0),-1)
        points.append((x,y))
        if len(points) >= 2:
            for i in range(len(points)):
                cv2.line(img,points[i-1],points[-1],(255,255,0),4)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        blue = img[y,x,0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        mycolorimage = np.zeros((512,512,3),np.uint8)
        cv2.circle(img,(x,y),10,(0,255,255),-1)
        mycolorimage[:] = [blue,red,green]
        cv2.imshow('image',img)
        cv2.imshow('colorwindow',mycolorimage)

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('messi.jpg')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
