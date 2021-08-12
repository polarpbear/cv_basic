# 尺度不变的特征检测
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# SIFT算法
'''
sift=cv.xfeatures2d.SIFT_create()  1.实例化

keypoint,description=sift.detectAndCompute(gray,None) 2.检测关键点
kp  位置,尺度,方向
des  含有128个梯度信息的特征向量

cv.drawKeypoints(image,keypoint,outputimage,color,flags)  3.绘制图像
flags   cv2.DRAW_MATCHES_FLAGS_DEFAULT 创建输出图像矩阵,使用现存输出图像绘制匹配对和特征点
        cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG 不创建输出图像矩阵，在输出图像上绘制匹配对
        cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS 对每一个特征点绘制带大小和方向的关键点图形
        cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS 单点特征点不绘制

'''

img=cv.imread('C:/Users/polarbear/Desktop/cv/tst.jpg')
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


sift=cv.xfeatures2d.SIFT_create()

kp,des=sift.detectAndCompute(img_gray,None)


cv.drawKeypoints(img,kp,img,(0,0,255),cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.imshow(img[:,:,::-1])
plt.show()



























