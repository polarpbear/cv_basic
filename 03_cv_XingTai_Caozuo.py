#形态学操作

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# 腐蚀
''' cv.erode(img,kernel,iterations)
结构、腐蚀次数
'''
# 膨胀
''' cv.dilate(img,kernel,iterations)
'''

#开运算
''' 先腐蚀，后膨胀，去除小噪点
'''
#闭运算
'''先膨胀,后腐蚀，填充孔洞
'''

# 礼帽
''' 原图与开运算的结果图之差
tophat(src,element)=src-open(src,element)
突出比临近点亮的班块
''' 

# 黑帽
''' 原图与闭运算结果图之差
blackhat(src,element)=close(src,element)-src
突出比临近点暗的版块
'''
# cv.morphologyEx(img,op,kernel) op选择模式
# cv.MORPH_OPEN 
# cv.MORPH_CLOSE
# cv.MORPH_TOPHAT
# cv.MORPH_BLACKHAT

img=cv.imread("C:/Users/polarbear/Desktop/cv/src_img.jpg",0)
tw=np.ones((25,25),np.uint8)
uit1=cv.add(tw,255)

res1=cv.morphologyEx(img,cv.MORPH_OPEN,uit1)
res2=cv.morphologyEx(img,cv.MORPH_CLOSE,uit1)
res3=cv.morphologyEx(img,cv.MORPH_TOPHAT,uit1)
res4=cv.morphologyEx(img,cv.MORPH_BLACKHAT,uit1)

fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(8,8),dpi=100)
axes[0][0].imshow(res1,cmap=plt.cm.gray)
axes[0][0].set_title("open")
axes[0][1].imshow(res2,cmap=plt.cm.gray)
axes[0][1].set_title("close")
axes[1][0].imshow(res3,cmap=plt.cm.gray)
axes[1][0].set_title("tophat")
axes[1][1].imshow(res4,cmap=plt.cm.gray)
axes[1][1].set_title("blackhat")
plt.show()
















