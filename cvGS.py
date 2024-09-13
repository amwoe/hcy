import numpy as np
import cv2 as cv
cap = cv.VideoCapture('view.MOV')
while cap.isOpened():
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    blurGS = cv.GaussianBlur(frame,(25,25),0)
    cv.imshow('frame', frame)
    cv.imshow('GS_frame', blurGS) 
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()