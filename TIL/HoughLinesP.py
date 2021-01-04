# 허브 변환 직선 검출

import cv2
import sys
import numpy as np

src = cv2.imread('field.bmp', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(src, 50 , 150)

lines = cv2.HoughLinesP(edges, 1.0, np.pi/180, 160, minLineLength =50, maxLineGap = 5)

dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]):
        pt1 = (lines[i][0][0], lines[i][0][1])
        pt2 = (lines[i][0][2], lines[i][0][3])
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()