import cv2
import matplotlib.pylab as plt
import numpy as np

def region_of_interest(img,vertical):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask,vertical,match_mask_color)
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image

def draw_the_lines(img,lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2),(0,255,0),thickness=4)
    img = cv2.addWeighted(img,0.8,blank_image,1,0.0)
    return img

#img = cv2.imread('road.jpg')
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
def process(img):
    height = img.shape[0]
    width = img.shape[1]
    #print(height,width)
    roi = [
        (100, height),
        (width/2-30,height/4*3-15),
        (int(width / 2),height / 4*3-15),
        (800, height)
    ]
    #print(roi)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 150, 200)
    cropped_image = region_of_interest(canny, np.array([roi], np.int32))
    cv2.imshow('crop',cropped_image)
    lines = cv2.HoughLinesP(cropped_image, 4, np.pi / 60, 50, np.array([]), 10, 40)
    img_with_lines = draw_the_lines(img, lines)
    return img_with_lines

def click(event,x,y,flage,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        frmae = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        b = frame[y,x,0]
        print(b)

cap = cv2.VideoCapture('lane_dection.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.setMouseCallback('frame',click)
    cv2.imshow('frame',frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,th = cv2.threshold(frame,65,95,cv2.THRESH_BINARY)
    cv2.imshow('th',th)
    if cv2.waitKey(40) == 27:
        break
cap.release()
cv2.destroyAllWindows()