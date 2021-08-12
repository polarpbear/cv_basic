# ORB算法
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# API 实例化
'''
orb=cv.xfeatures2d.orb_create(nfeatures)
nfeatures 特征点最大数量

'''
# 检测关键点
'''
kp,des=orb.detectAndCompute(gray,None)

gray 灰度图像
des 描述符，二进制字符串

使用Fast检测关键点，然后以特征点到质心方向为主方向
BRIEF计算关键点数量
'''


img=cv.imread('C:/Users/polarbear/Desktop/cv/line_tst.jpg')
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


orb=cv.ORB_create(1000)

kp,des=orb.detectAndCompute(img_gray,None)

out_img=cv.drawKeypoints(img,kp,None,(0,0,255))


plt.imshow(out_img[:,:,::-1])
plt.show()




