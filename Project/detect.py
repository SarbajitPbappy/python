import cv2
import imutils
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

image=cv2.imread('test.jpg')
image=imutils.resize(image,width=min(400,image.shape[1]))

(rects,weights)=hog.detectMultiScale(image,winStride=(4,4),padding=(8,8),scale=1.05)
for (x,y,w,h) in rects:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()