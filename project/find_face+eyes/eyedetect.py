import sys
import numpy as np
import cv2


src = cv2.imread('love.jpeg')

if src is None:
    print('no img')
    sys.exit()

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')

if face_classifier.empty() or eye_classifier.empty():
    print('no xml')
    sys.exit()

faces = face_classifier.detectMultiScale(src, minSize= (100,100))

for (x1, y1, w1, h1) in faces:
    cv2.rectangle(src, (x1, y1, w1, h1),(255, 0, 255),2 )

    faceROI = src[y1: y1 + h1//2, x1:x1 + w1]
    eyes =eye_classifier.detectMultiScale(faceROI)

    for (x2, y2, w2, h2) in eyes:
        center = (x2 + w2 //2, y2 + h2 // 2)
        cv2.circle(faceROI, center, w2//2, (255, 0, 0 ), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()