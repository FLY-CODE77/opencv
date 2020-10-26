import sys
import cv2

cap = cv2.VideoCapture(0)
# camer on !!

if not cap.isOpened():
    print('cam dead')
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# import cam size
# round it beacuse frame values is float

fps = cap.get(cv2.CAP_PROP_FPS)
# get fps

fourcc =cv2.VideoWriter_fourcc(*'DIVX')
# *'DIVX' = 'D','I','V','X'
delay = round(1000/fps)

out = cv2.VideoWriter('output.avi',fourcc,fps,(w,h))
# VideoWriter make out class to write video

while True:
    ret,frame = cap.read()

    if not ret:
        break   
    out.write(frame)

    cv2.imshow('frame',frame)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

