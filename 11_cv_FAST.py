# FAST算法
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# API 实例化
'''
fast=cv.FastFeatureDetector_create(threshold,nonmaxSuppression)
threshold 阈值默认10
nonmaxSuppression 是否进行非极大值抑制，默认True

'''

# 检测关键点
'''
kp=fast.detect(grayImg,None)

点周围圆周上有一定数量点与该点像素不同，则认为是关键点
'''

# 绘制图像
'''
cv.drawKeypoints(image,keypoints,outputimg,color,flags)

'''
img=cv.imread('C:/Users/polarbear/Desktop/cv/line_tst.jpg')
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

fast=cv.FastFeatureDetector_create(threshold=30,nonmaxSuppression=True)

kp=fast.detect(img_gray,None)
img2=cv.drawKeypoints(img,kp,None,(0,0,255))

fast.setNonmaxSuppression(0)
kp2=fast.detect(img_gray,None)
img3=cv.drawKeypoints(img,kp2,None,(0,0,255))

plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121)
plt.imshow(img2[:,:,::-1])
plt.subplot(122)
plt.imshow(img3[:,:,::-1])
plt.show()




