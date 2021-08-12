# 霍夫检测
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#霍夫直线检测
'''
cv.HoughLines(img,rho,theta,threshold)
img 二值化图像
rho,theta精度
threshold 阈值，高于阈值才认为是直线
'''

#霍夫圆检测
'''
circles=cv.HoughCircles(image,method,dp,minDist,param1=100,param2=100,minRadius=0,maxRadius=100)
image 灰度图像，已封装canny边缘检测
method cv.HOUGH_GRADIENT
dp 霍夫空间分辨率=原图分辨率/2
minDist 圆心间最小距离，小于该值认为是同一个圆心
param1 canny检测阈值 低阈值为高阈值一半
param2 检测圆心,半径阈值,共用
circles 圆心横坐标,纵坐标，圆半径
对噪声敏感，需要进行滤波
'''


# 直线检测demo
'''
img=cv.imread('C:/Users/polarbear/Desktop/cv/line_tst.jpg')

img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges=cv.Canny(img_gray,50,150) #canny边缘检测

lines=cv.HoughLines(edges,0.8,np.pi/180,150)

for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+2000*(-b))
    y1=int(y0+2000*(a))
    x2=int(x0-2000*(-b))
    y2=int(y0-2000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255))

plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121)
plt.imshow(img[:,:,::-1])
plt.subplot(122)
plt.imshow(edges,cmap=plt.cm.gray)
plt.show()
'''

# 霍夫圆检测demo
img=cv.imread('C:/Users/polarbear/Desktop/cv/circle.jpg')

img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
circles=cv.HoughCircles(img_gray,cv.HOUGH_GRADIENT,1,200,param1=100,param2=20,minRadius=5,maxRadius=200)

for circ in circles[0,:]:
    cv.circle(img,(int(circ[0]),int(circ[1])),int(circ[2]),(0,0,255),2)
    cv.circle(img,(int(circ[0]),int(circ[1])),2,(255,0,0),-1)

plt.imshow(img[:,:,::-1])
plt.title('hough_circle_tst')
plt.show()

#img_c=cv.medianBlur(img_gray,3)












