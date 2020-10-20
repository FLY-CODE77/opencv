import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8) # 흰색으로 채워져있는 영상 

cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5) #가로로 150 정도의 직선을 그리겠다 색은 빨간색 두깨는 5
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2) # 좌측 상단에서 시작 가로로 150 세로로 100 의 사각형  색깔은 녹색 선은 2
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1) # 좌측 상단 -> 우측 하단 좌표 찍어주고, 색깔은 짙은 녹색 선은 
                                                            # -1 thickness에 음수를 지정하면 사각형 내부를 채운다(다각형 모형에서만 동작)
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA) # 중심점 좌표를 불러 주고 30의 반지름을 가지고 내부를 채운다 cv2.line_8 은 조금 거친 직선 느낌이 난다
                                                                # CV2,LINE_AA 로 강제로 조금 스무딩 시켜주는 역활을 시켜서 도형을 그린다
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]]) # 4개의 점을 2차원 행렬로 저장
cv2.polylines(img, [pts], True, (255, 0, 255), 2) #pts 는 넘파이 어래이를 '리스트 형태로 넣어서' 도형을 그리기로 한다 
                                                 # IS CLOSED : TRUE를 주면 폐곡선을 닫는 느낌 FALSE 는 안 닫고 그냥 그리는 느낌으로 간다

text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8,  #X,Y 좌표 표시해줘서 간다!!
            (0, 0, 255), 1, cv2.LINE_AA) # LINE_AA 함수를 넣어주면 깔끔한 이쁜 녀석이 된다

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

