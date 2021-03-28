import numpy as np
import cv2
import datetime
#lessen5

#img = cv2.imread('messi.jpg', 1)
"""img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img, (0,0),(20,255), (255, 255, 0),15)
img = cv2.arrowedLine(img,(50,50),(20,255),(100,100,100),20)
img = cv2.rectangle(img,(100,100),(20,255),(200,200,200),-1)
img = cv2.circle(img,(200,200),50,(10,10,10),-1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'Opencv',(10,60),font,4,(60,60,0),cv2.LINE_AA)


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()"""

#lessen6,7

cap = cv2.VideoCapture(0)
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3,700)
#cap.set(4,700)
#print(cap.get(3))
#print(cap.get(4))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font = cv2.FONT_HERSHEY_SIMPLEX
        datet = str(datetime.datetime.now())
        text = 'Width: '+str(cap.get(3)) + 'Height: '+str(cap.get(4))
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        frame = cv2.rectangle(frame,(150,150),(300,300),(50,50,50),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()