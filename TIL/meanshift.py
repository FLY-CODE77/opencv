import sys
import numpy as numpy
import cv2

# video file open
cap = cv2.VideoCapture('camshift.avi')

if not cap.isOpened():
    print('Video open failed')
    sys.exit()


# intial rect
x, y, w, h = 135, 220, 100, 100
rc =(x, y, w, h)

ret, frame = cap.read()
if not ret:
    print('frame read fail!')
    sys.exit()

roi = frame[y:y+h, x:x+w]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# calc histogram
channels = [0,1]
ranges = [0, 180, 0, 256]
hist = cv2.calcHist([roi_hsv], channels, None, [90,128], ranges)


# Set Mean Shift end points
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # HS HISTOGRAM BACKPROPAGATIOON    
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    backproj = cv2.calcBackProject([frame_hsv], channels, hist, ranges, 1)

    # Mean Shift
    _, rc = cv2.meanShift(backproj, rc, term_crit)

    # print 
    cv2.rectangle(frame, rc, (0,0,255), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(60) == 27:
        break
cap.release()
cv2.destroyAllWindows()