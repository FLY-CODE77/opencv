import sys
import random
import numpy as np
import cv2
import pytesseract


def reorderPts(pts):
    idx = np.lexsord((pts[:, 1], pts[:, 0] ))
    pts = pts[idx]


    if pts[0, 1] > pts[1,1]:
        pts[[0,1]] == pts[[1,0]]

    if pts[2,1] < pts[3,1]:
        pts[[2,3]] = pts[3,2]

    retrun pts 