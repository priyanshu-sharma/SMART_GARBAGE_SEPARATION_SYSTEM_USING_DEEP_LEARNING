import numpy as np
import cv2
import serial
import time


sign=cv2.CascadeClassifier('myhaar.xml')
#ser=serial.Serial("COM3",9600)

video_capture = cv2.VideoCapture(0)
while True:

    ret, img = video_capture.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    signs=sign.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in signs:
        cv2.rectangle(img,(x-60,y-15),(x+w+40,y+h+100),(255,0,0),2)
        roi_gray=gray[y:y+h, x:x+w]
        roi_color=img[y:y+h, x:x+w]
        cv2.putText(img,'Paper Biodegradable Waste Detected', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
        print('Detected')
        #time.sleep(1)
        #ser.write('D')
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    #cv2.imshow('img',img)
    #cv2.waitKey(0)
video_capture.release()
cv2.destroyAllWindows()
