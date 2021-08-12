# 边缘检测
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 一阶导数求极值
'''
sobel算子
[-1,-2,-1
0,0,0
1,2,1]y向 x向转置
scharr算子
[-3,-10,-3
0,0,0
3,10,3]y向 x向转置

cv.Sobel(src,ddepth,dx,dy,dst,ksize,scale,delta,borderType)
ddepth cv.CV_16S 将图像数据类型转为16位有符号
dx,dy 1或0
ksize 卷积核大小,默认3 -1为scharr算子
scale 缩放比例常数，默认无缩放

'''

# 二阶导数求极值
'''
Laplacian算子
[0,1,0
1,-4,1
0,1,0]

cv.Laplacian(src,ddepth[,dst[,ksize[,scale[,delta[,boderType]]]]])

'''

# canny边缘检测
'''
第一步 噪声去除
第二步 计算图像梯度
边缘的像素点梯度与边缘垂直
第三步 非极大值抑制
第四步 滞后阈值
灰度梯度高于maxval认为是真正的边界，灰度梯度低于minval抛弃
介于两者之间若与真边界相连则是真边界
canny=cv.Canny(img,minval,maxval)

'''




img_gray=cv.imread("C:/Users/polarbear/Desktop/cv/tst.jpg",0)


# 计算一阶导数卷积 cv.CV_16S会将数据变成16位有符号
'''
x=cv.Sobel(img_gray,cv.CV_16S,1,0)
y=cv.Sobel(img_gray,cv.CV_16S,0,1)
scx=cv.Sobel(img_gray,cv.CV_16S,1,0,ksize=-1)
scy=cv.Sobel(img_gray,cv.CV_16S,0,1,ksize=-1)
# 数据转换
abx=cv.convertScaleAbs(x)
aby=cv.convertScaleAbs(y)
scabx=cv.convertScaleAbs(scx)
scaby=cv.convertScaleAbs(scy)
# 结果合成
res=cv.addWeighted(abx,0.5,aby,0.5,0)
res2=cv.addWeighted(scabx,0.5,scaby,0.5,0)

plt.figure(figsize=(10,8),dpi=100)
plt.subplot(131)
plt.imshow(img_gray,cmap=plt.cm.gray)
plt.title('before')
plt.xticks([])
plt.yticks([])
plt.subplot(132)
plt.imshow(res,cmap=plt.cm.gray)
plt.title('sobel')
plt.xticks([])
plt.yticks([])
plt.subplot(133)
plt.imshow(res2,cmap=plt.cm.gray)
plt.title('scharr')
plt.xticks([])
plt.yticks([])
plt.show()
'''

# 计算二阶导数卷积

res=cv.Laplacian(img_gray,cv.CV_16S)
Scale_abs=cv.convertScaleAbs(res)
canny=cv.Canny(img_gray,0,100)

plt.figure(figsize=(10,8),dpi=100)
plt.subplot(131)
plt.imshow(img_gray,cmap=plt.cm.gray)
plt.title('before')
plt.xticks([])
plt.yticks([])
plt.subplot(132)
plt.imshow(Scale_abs,cmap=plt.cm.gray)
plt.title('laplacian')
plt.xticks([])
plt.yticks([])
plt.subplot(133)
plt.imshow(canny,cmap=plt.cm.gray)
plt.title('Canny')
plt.xticks([])
plt.yticks([])
plt.show()

























