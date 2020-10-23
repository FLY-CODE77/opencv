# opencv 카메라 열기 동영상 처리하기
import sys
import cv2


# 카메라 열기
# cap = cv2.VideoCapture() #객체 생성해주기
# cap.open(0) # 0번 카메라를 실행하겠다
cap = cv2.VideoCapture(0) # 하나로 가능

# 카메라를 열 때는 숫자값이 들어가고 () 사이 , 동영상을 열 때는 (동영상 이름) 이 들어간다
# 카메라 열기 
# cv2.videoCapture(index,apiPreference =None) -> retval
# index -- 0 으로 열면 카메라에 기본 카메라 오픈 만약 두대가 있으면 하나는 0 번 하나는 1번
# cv2.VideoCapture.isOpend() --> retval 
# 비디오 캡쳐가 준비 되었는지 확인한다 성공이면 1 아니면 0
# 프레임 받아오기
# cv2.videoCapture.read(imgae=None) --> retval,image : 성공하면 1 아니면 0 
# image numpy.ndarray --> 현재프레임
if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) # cap.get() : 카메라의 속성을 받아 오는거 
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) 
# 카메라 사이즈 조절 
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
# 카메라 프레임 처리 

while True:
    ret, frame = cap.read()
#cap.read() 는 BOOL,FRAME BOOL 카메라 정보가 제대로 받아 왔는지 체크도 하고 들어온다
    if not ret:
        break
    edge =cv2.Canny(frame,50,150)
    cv2.imshow('frame', frame)
    cv2.imshow('frame', edge)
    # 선으로 표시 해주는거 EDGE

    #inversed = ~frame  # 반전

    # cv2.imshow('frame', frame) # 반전이 안되어 있다
   

    if cv2.waitKey(10) == 27: # 20MS 안에 키를 치면 프레임 넣어주면 빠져 나온다 27 :ESC
        break

cap.release() # cap이라는 변수를 릴리즈 
cv2.destroyAllWindows() # 모든창을 닫는 형태

