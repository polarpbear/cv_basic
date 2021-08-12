# 模板匹配
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# 模板匹配
'''
res=cv.matchTemplate(img,template,method)
template 模板
method CV_TM_SQDIFF 平方差匹配
CV_TM_CCORR 乘法匹配，相似度
CV_TM_CCOEFF 相关系数匹配 1完美 -1最差匹配

cv.minMaxLoc() 找出最大最小值位置
'''

img=cv.imread("C:/Users/polarbear/Desktop/cv/tst.jpg")
template=cv.imread("C:/Users/polarbear/Desktop/cv/template.jpg")

h,w,l=template.shape

# 相关度匹配
res=cv.matchTemplate(img,template,cv.TM_CCORR)
# 平方差匹配
res2=cv.matchTemplate(img,template,cv.TM_SQDIFF)
# 极值定位
min_val,max_val,min_loc,max_loc=cv.minMaxLoc(res)
min_val2,max_val2,min_loc2,max_loc2=cv.minMaxLoc(res2)

top_left=max_loc
bottom_right=(top_left[0]+w,top_left[1]+h)
cv.rectangle(img,top_left,bottom_right,(0,0,255),3)

top_left2=min_loc2
bottom_right2=(top_left2[0]+w,top_left2[1]+h)
cv.rectangle(img,top_left2,bottom_right2,(255,0,0),2)

plt.imshow(img[:,:,::-1])
plt.title('result')
plt.xticks([])
plt.yticks([])
plt.show()
