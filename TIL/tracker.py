import sys
import numpy as np
import cv2

cap = cv2.VideoCapture('/home/flycode77/code/opencv/ch10/tracking2.mp4')

if not cap.isOpened():
    print('video error')
    sys.exit()

# tracker class make

# KCF is fast algorism but not accuracy
#tracker = cv2.TrackerKCF_create()

# CSRT is accuracy algorism but low speed
tracker = cv2.TrackerCSRT_create()

ret, frame = cap.read()

if not ret:
    print("frame error")
    sys.exit()

rc = cv2.selectROI('frame', frame)
tracker.init(frame, rc)


while True:
    ret, frame = cap.read()

    if not ret:
        print('frame read Failed!')
        sys.exit()

    #tracking & roi rect update
    ret, rc = tracker.update(frame)
    rc = tuple([int(_) for _ in rc])
    cv2.rectangle(frame, rc, (0, 0, 255), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()