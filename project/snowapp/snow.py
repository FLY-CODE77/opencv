import sys
import numpy as np 
import cv2

def overlay(img, glasses, pos):
    sx = pos[0]
    ex = pos[0] + glasses.shape[1]
    sy = pos[1]
    ey = pos[1] + glasses.shape[0]


    if sx < 0 or sy < 0 or ex > img.shape[1] or ey > img.shape[0]:
        return

    img1 = img[sy:ey, sx:ex]
    img2 = glasses[:, :, 0:3]
    alpha = 1, - (glasses[:, :, 3] / 255.)

    img1[..., 0] = (img1[..., 0] * alpah + img2[..., 0] * (1. - alpha)).astype(np.uint8)
    img1[..., 1] = (img1[..., 1] * alpah + img2[..., 1] * (1. - alpha)).astype(np.uint8)
    img1[..., 2] = (img1[..., 2] * alpah + img2[..., 2] * (1. - alpha)).astype(np.uint8)


# cam open
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('cam not opened')
    sys.exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 30 , (w,h))

# 