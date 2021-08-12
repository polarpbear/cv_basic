import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 基础加减操作和变换

# 图像加法
# cv.add(A1,A2) A1,A2均为图像

#图像混合
'''cv.addWeighted(A1,k1,A2,k2,z)  = (k1*A1+k2*A2)+z偏置
'''

#图像缩放
'''cv.resize(src,dsize,fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
# dsize 绝对尺寸
# fx,fy 相对尺寸与绝对尺寸只需一个
# cv2.INTER_LINEAR 线性
#NEAREST 最近邻插值
#AREA 像素区域重采样（默认）
#CUBIC 双三次
'''

# 图像平移
'''M=np.float32([1,0,dtx],[0,1,dty])
# dsize 输出图像大小[width,height]
# cv.warpAffine(img,M,dsize)
'''

# 图像旋转
# M=cv.getRotation(center,angle(deg),scale(缩放大小=0.x,1))

# 仿射变换
# 变换矩阵M=[A B]=([a00 a01 b0],[a10,a11,b1])
# 执行A*(x,y)+B=M*(x,y,1)
# 求解矩阵
pt1=np.float32([[50,50],[200,50],[50,200]])#仿射前位置
pt2=np.float32([[100,100],[200,50],[100,250]])#仿射后位置
M=cv.getAffineTransform(pt1,pt2)

#透射变换
pts1=np.float32([[56,65],[368,52],[28,387],[389,390]])#透射前位置
pts2=np.float32([[100,145],[300,100],[80,290],[310,300]])#透射后位置
T=cv.getPerspectiveTransform(pts1,pts2)

# 图像金字塔
# 上采样 up_img=cv.pyrUp(img) 分辨率增加
# 下采样 dow_img=cv.pyrDown(img) 分辨率减少

img=cv.imread("C:/Users/polarbear/Desktop/cv/src_img.jpg",1)

#缩小一倍
rows,cols=img.shape[:2]
cols=int(cols*0.5)
rows=int(rows*0.5)
res=cv.resize(img,(cols,rows),interpolation=cv.INTER_LINEAR)

#加入文字图片，合成
tw=np.ones((rows,cols,3),np.uint8)
tw=cv.add(tw,50)
text='beauty'
station=[50,100]
font=cv.FONT_HERSHEY_COMPLEX
fontsize=2
color=[100,100,200]
thickness=5
cv.putText(tw,text,station,font,fontsize,color,thickness,cv.LINE_AA)

#rel=cv.add(res,tw)
rel=cv.addWeighted(res,0.4,tw,0.6,0)

# 仿射变换
ref=cv.warpAffine(res,M,(cols,rows))

# 投射变换
ret=cv.warpPerspective(res,T,(cols,rows))

fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(6,6),dpi=100)
axes[0][0].imshow(res[:,:,::-1])
axes[0][0].set_title("before")
axes[0][1].imshow(rel[:,:,::-1])
axes[0][1].set_title("after")
axes[1][0].imshow(ref[:,:,::-1])
axes[1][0].set_title("affine")
axes[1][1].imshow(ret[:,:,::-1])
axes[1][1].set_title("perspective")
plt.show()
