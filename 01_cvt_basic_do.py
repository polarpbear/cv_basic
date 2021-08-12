import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 基础操作，添加几何图形，文字,修改数值

img=cv.imread("C:/Users/polarbear/Desktop/cv/tst.jpg",1)
# 1彩色模式（默认) 0灰度模式 -1 包含alha通道的图像模式


#cv.imshow("name",img)
#cv.waitKey(0)

# 保存文件
#cv.imwrite("tst_name.png",img)

# 绘制直线
# cv.line(img,start,end,color,thickness)

# 绘制圆形
#cv.circle(img,centerpoint,radius,color,thickness)
#thickness -1时闭合并填充

# 绘制矩形
#cv.rectangle(img,leftupper,rightdown,color,thickness)

# 添加文字
#cv.putText(img,text,station,font,fontsize,color,thickness,cv.LINE_AA)
text='beaut'
station=[50,100]
font=cv.FONT_HERSHEY_COMPLEX
fontsize=3
color=[100,100,200]
thickness=3
cv.putText(img,text,station,font,fontsize,color,thickness,cv.LINE_AA)

# 图像属性
#img. shape size dtype

# 通道拆分
b,g,r=cv.split(img)
# 通道合并
img=cv.merge((b,g,r))
# 色彩空间改变 记得赋值
# cv.cvtColor(input_image,flag)
#flag-> cv.COLOR_BGR2GRAY 灰度    cv.COLOR_BGR2HSV
img_hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

                
plt.imshow(img[:,:,::-1])
plt.show()
