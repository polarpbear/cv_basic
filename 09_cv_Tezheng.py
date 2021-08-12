# 特征检测
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 角点检测原理
'''
E(u,v)=sum([x,y],w(x,y)*((I(x+u,y+v)-I(x,y))^2))
w(x,y) 窗口函数 矩形窗口，高斯型窗口
I(x+u,y+v) 平移后灰度
I(x,y) 局部窗口灰度
利用I(x+u,y+v)一阶泰勒展开，舍去余项，化简为二次型
E(u,v)=[u,v].*sum([x,y],w(x,y)*[Ix*Ix,Ix*Iy;Ix*Iy,Iy*Iy]).*[u;v]
=[u,v].*M.*[u;v]
求解M特征向量，得出变化率最大和最小两个方向

两特征值都较大时，为角点
两特征值都较小时，为平面
两特征值一个较大、一个较小时，为边缘
'''

# Harris角点检测
'''
计算角点相应值判断
R=det(M)-a*(traceM)^2
detM=nemda1*nemda2
traceM=nemda1+nemda2
a 为常数

R<0 边缘
abs(R)<ep 平面
R>0  角点

cv.cornerHarris(src,blockSize,ksize,k)
src float32型输入图像
blockSize 角点检测的邻域
ksize sobel求导大小
k 角点检测自由参数 0.04~0.06

'''
# 角点检测
'''
img=cv.imread('C:/Users/polarbear/Desktop/cv/line_tst.jpg')
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray32=np.float32(img_gray)

dst=cv.cornerHarris(gray32,5,3,0.004)

img[dst>0.001*dst.max()]=[0,0,255]

plt.imshow(img[:,:,::-1])
plt.title('Harris')
plt.xticks([])
plt.yticks([])
plt.show()
'''

# Shi-Tomasi角点检测
'''
若较小的特征值大于阈值，认为是角点
cv.goodFeaturesToTrack(img,maxcorners,qualityLevel,minDistance)
img 灰度图
maxcorners 设置角点数目
qualityLevel 可接受的角点质量水平 0~1
minDistance 角点间的最小欧式距离

'''
img=cv.imread('C:/Users/polarbear/Desktop/cv/line_tst.jpg')
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

coners=cv.goodFeaturesToTrack(img_gray,1000,0.01,15)

for pit in coners:
    x,y=pit.ravel()
    cv.circle(img,(int(x),int(y)),2,(0,0,255),-1)

plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1])
plt.title('Shi_Tomas')
plt.show()















