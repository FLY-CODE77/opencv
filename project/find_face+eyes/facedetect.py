import sys
import numpy as np
import cv2

src = cv2.imread('love.jpeg')

if src is None:
    print('no img')
    sys.exit()

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

if classifier.empty():
    print('no Xml')
    sys.exit()

faces = classifier.detectMultiScale(src,minSize=(100,100))

for (x,y,w,h) in faces:
    face_img = src[y : y + h, x: x + w]
    cv2.rectangle(src, (x,y,w,h), (255, 0 ,255), 2)

cv2.imshow('src', src)
cv2.imshow('img', face_img)
cv2.waitKey()
cv2.destroyAllWindows()