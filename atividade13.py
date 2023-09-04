# coding=utf-8
import numpy as np
import cv2,sys

cap = cv2.VideoCapture("videos/IFMA Campus Caxias.mp4")
if not cap.isOpened():
    print("Erro ao abrir a camera")
    sys.exit(0)

face_cascade = cv2.CascadeClassifier('classificadores/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('classificadores/haarcascade_eye.xml')
#mouth_cascade = cv2.CascadeClassifier('classificadores/haarcascade_mcs_mouth.xml')

#cv2.namedWindow('Cam')
pessoas = 0
while True:
    ret, frame = cap.read()
    img = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imshow('Webcam', img)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
