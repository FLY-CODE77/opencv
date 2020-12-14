import sys
import numpy as np
import cv2

def cartoon_filter(img):
    
    h, w = img.shape[:2]
    img = cv2.resize(img,(w//2, h//2))
    # 사이즈를 줄여서 시작 
    # 계산을 줄여야하니깐!

    blr = cv2.bilateralFilter(img, -1, 10, 6)
    # canny 는 컬러를 받아도 자동으로 그레이 스케일 화 한다
    edge = 255 - cv2.Canny(img, 50, 110)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    
    dst = cv2.bitwise_and(blr, edge)

    # 다시 늘리기 , 갑이 급격하게 바뀌는 느낌이 있을수 있으니까
    dst = cv2.resize(dst, (w,h), interpolation = cv2.INTER_NEAREST)
    
    return dst

def pencil_sketch(img):
    # 평탄한 영역은 흭색
    # 에지 근방에서는 어두운 영역을 검정색으로 설정 
    # 밝은 영역은 흰색
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, (0,0), 3)
    dst = cv2.divide(gray, blr, scale= 255)
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    return dst

cap = cv2.VideoCapture('video1.mp4')
#cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print('no cam')
    sys.exit()

cam_mode = 0 

while True:
    ret,frame = cap.read()


    if not ret:
        break
    
    if cam_mode == 1:
        frame = cartoon_filter(frame)

    elif cam_mode == 2:
        frame = pencil_sketch(frame)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27 :
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0