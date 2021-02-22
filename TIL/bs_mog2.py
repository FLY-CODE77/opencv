import sys
import numpy as np
import cv2


cap = cv2.VideoCapture('PETS2000.avi')

if not cap.isOpened():
    print('video wrong')
    sys.exit()

bs = cv2.createBackgroundSubtractorMOG2()
# knn method backgroundSubtractor
# bs = cv2.createBackgroundSubtractorKNN()
# don't care about shadows 
# bs.setDetectShadows(False)


while True:
    ret , frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    fgmask = bs.apply(gray)
    back = bs.getBackgroundImage()

    cnt, _, stats, _ = cv2.connectedComponentsWithStats(fgmask)

    for i in range(1, cnt):
        x, y, w, h, s = stats[i]

        if s <80:
            continue
        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('back', back)
    cv2.imshow('fgmask', fgmask)
    if cv2.waitKey(30) == 27:
        break
cap.release()
cv2.destroyAllWindows()