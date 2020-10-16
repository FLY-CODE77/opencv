import sys
import cv2

print('hello,open Cv',cv2.__version__)

img = cv2.imread('cat.bmp',cv2.IMREAD_ANYDEPTH)
# img = cv2.imwrite('cat_gray.png',img) # cv2.imwrite(filename.img,.params = None) -->  numpy 화

print(img)

if img is None:
    print('Image load failed')
    sys.exit()

cv2.namedWindow('image') # Default 값은 영상의 크기에 맞게 끔 Auto로 조절 되어있다. --> 사이즈 조절 가능 x
# flag : window = normal --> 마우스 크기에 맞게 끔 사이즈 조절 가능     
cv2.imshow('image',img)
cv2.waitKey()  #  키 눌르기 전 까지 영상 유지 시켜 주는 함수
cv2.destroyAllWindows() # 모든 창을 다 닫아준다
# 윈도우에서는 창 하나 하나를 핸들 하는데 (정수형), OPENCV에서는 창 하나 하나를 str형으로 받기 떄문에 'image'가 가능하다

# 순서는 윈도우를 만들고 == > imshow 이미지를 불러오는게 문법
# waitKey() 가 없으면 화면이 뜨지 않는다.! 키를 기달릴 뿐만 아니라 화면에 뜨기 까지 기달린다



