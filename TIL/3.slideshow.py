#images 는 폴더 입니다 
import os 
file_list = os.listdir('.\\images') # 파일 목록 다 불러 올수 있는 코드
img_files = [file for file in file_list if file.endswith('.jpg')]
import glob
img_files = glob.glob('.\\images\\*.jpg')
# glob 이라는 명령어를 사용하면 그 안에 있는 특정 패턴을 파일들 모두 불러오기 가능 
for f in img_files:
    print(f)

# 파일들이 잘 들어 가 있는 것을 알수 있음

import cv2 
# 전체 화면으로 영상 출력 창 만들기 코드

# cv2.WINDOW_NORMAL 속성의 창을 만들고 cv2.setWindowProperty() 함수를 사용 전체 화면 속성으로 변경 시켜 준다 .
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('image',cv2.WND_PROP_FULLSCRESSN, cv2.WINDOW_FULLSCREEN) 
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

# 이제 창을 뛰우기 까지 성공

# 무한 루프를 사용한 영상 올리기
cnt = len (img_files)
idx = 0 

# 무한 루프 중단을 위한 파일 갯수 알아오기 CNT
while True:
    img = cv2.imread(img_files[idx])

    cv2.imshow('image',img)
    
    # 파일 없을 때 브레이크 
    if img is None:
        print('Image load failde')
        break 

    if cv2.waitKey(1000) == 27: #ESC 
    # if cv2.waitKey(1000) >=0: 0보다 같거나 크다면 -- > 아무 키나 잡아도 이미지 슬라이드가 종료 된다. 
    # 1000 MS ---> 1 초 동안 !! 아무 일 이 없다면 . 
        break
    idx +=1
    if idx>= cnt:
        idx =0

cv2.destroyAllWindows()