import sys
import numpy as np
import sys
import cv2
import random

cap = cv2.VideoCapture('vtest.avi')


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret , frame = cap.read()

    if not ret:
        break
    
    detected, _ = hog.detectMultiScale(frame)

    for (x, y, w, h) in detected:
         c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
         cv2.rectangle(frame, (x,y,w,h), c, 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()