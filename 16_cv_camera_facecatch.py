# 人脸识别
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# print(cv.__file__)  查找策略位置

# 1 读取摄像头
cap = cv.VideoCapture(0)

# 2 实例化人脸检测的分类器对象
'''
# 实例化级联分类器
classifier=cv.CascadeClassfier('C:/Python3/Python39/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# 加载分类器
classifier.load('haarcascade_frontalface_default.xml')
'''
face_cas=cv.CascadeClassifier('C:/Python3/Python39/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
face_cas.load('C:/Python3/Python39/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

eye_cas=cv.CascadeClassifier('C:/Python3/Python39/lib/site-packages/cv2/data/haarcascade_eye.xml')
eye_cas.load('C:/Python3/Python39/lib/site-packages/cv2/data/haarcascade_eye.xml')

# 3 进行人脸检测
'''
rect =classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize,maxsize)
scaleFactor 前后两侧扫描中，搜索窗口的比例系数
minNeighbors 最小检测次数
minSize,maxsize 目标最小与最大尺寸
'''
while(True):
    ret,frame = cap.read()
    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faceRets=face_cas.detectMultiScale(img_gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))
    for face in faceRets:
        x,y,w,h=face
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        eyeRets=eye_cas.detectMultiScale(img_gray[x:x+w,y:y+h])
        for eye_unit in eyeRets:
            ex,ey,ew,eh=eye_unit            
            cv.rectangle(frame,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)

                
    cv.imshow('frame',frame)
    
    if cv.waitKey(60) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()




