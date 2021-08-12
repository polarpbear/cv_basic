# 人脸识别
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# print(cv.__file__)  查找策略位置

# 1 读取图片，转换为灰度图
img=cv.imread('C:/Users/polarbear/Desktop/cv/face_tst.jpg')
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# 2 实例化人脸检测的分类器对象
'''
# 实例化级联分类器
classifier=cv.CascadeClassfier('C:/Python3/Python39/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# 加载分类器
classifier.load('haarcascade_frontalface_default.xml')
'''
face_cas=cv.CascadeClassifier('C:/Python3/Python39/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
face_cas.load('C:/Python3/Python39/lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# 3 进行人脸检测
'''
rect =classifier.detectMultiScale(gray,scaleFactor,minNeighbors,minSize,maxsize)
scaleFactor 前后两侧扫描中，搜索窗口的比例系数
minNeighbors 最小检测次数
minSize,maxsize 目标最小与最大尺寸
'''

faceRets=face_cas.detectMultiScale(img_gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))

for face in faceRets:
    x,y,w,h=face
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

plt.imshow(img[:,:,::-1])
plt.show()



