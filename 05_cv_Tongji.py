# 直方图统计
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 直方图统计
'''
cv.calcHist(images,channels,mask,histSize,ranges[,hist[,accumulate]])
channels 灰度图[0]，彩色 B[0] G[1] R[2]
mask 掩膜图像
histSize BIN数目 如[256]
ranges 像素值范围[0,256]
'''

# 直方图均衡化
'''
cv.equalizeHist(img)
img 灰度图
'''
# 自适应均衡化
'''
clahe=cv.createCLAHE(clipLimit=x,tileGridSize=(8,8))
对比度默认阈值40，tile块大小默认8*8
创建自适应均衡对象
cl1=clahe.apply(img)

'''
img_gray=cv.imread("C:/Users/polarbear/Desktop/cv/tst.jpg",0)

# 灰度与颜色统计
'''
img=cv.imread("C:/Users/polarbear/Desktop/cv/tst.jpg",1)
img_b,img_g,img_r=cv.split(img)
hist_gray=cv.calcHist([img_gray],[0],None,[256],[0,256])
hist_b=cv.calcHist([img_b],[0],None,[256],[0,256])
hist_g=cv.calcHist([img_g],[0],None,[256],[0,256])
hist_r=cv.calcHist([img_r],[0],None,[256],[0,256])
plt.plot(hist_gray,'k',label='gray')
plt.plot(hist_b,'b',label='blue')
plt.plot(hist_g,'g',label='green')
plt.plot(hist_r,'r',label='red')
plt.legend()
plt.grid()
plt.savefig('C:/Users/polarbear/Desktop/cv/plot_ex.png',dpi=300)
plt.show()
'''
#创建掩膜
'''
mask=np.zeros(img_gray.shape[:2],np.uint8)
mask[100:200,200:300]=255
mask_img=cv.bitwise_and(img,img,mask=mask)
plt.imshow(mask_img)
plt.show()
'''
res1=cv.equalizeHist(img_gray)
clahe=cv.createCLAHE(clipLimit=4.0,tileGridSize=(8,8))
res2=clahe.apply(img_gray)

fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(9,4),dpi=100)
axes[0].imshow(img_gray,cmap=plt.cm.gray)
axes[0].set_title("before")
axes[1].imshow(res1,cmap=plt.cm.gray)
axes[1].set_title("equalize")
axes[2].imshow(res2,cmap=plt.cm.gray)
axes[2].set_title("clahe")
plt.show()



















