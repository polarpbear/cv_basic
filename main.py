# 读取答题卡

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def sort_contours(cnts,method='left2right'):
    reverse=0
    i=0
    if method=='right2left' or method=='bottom2top':
        reverse=1
    if method=='top2bottom' or method=='bottom2top':
        i=1
    boundingBoxes=[cv.boundingRect(c) for c in cnts]
    (cnts,boundingBoxes)=zip(*sorted(zip(cnts,boundingBoxes),
                                     key=lambda b: b[1][i], reverse=reverse))
    return cnts,boundingBoxes

# 正确答案
crct_ans={0:[1],1:[4],2:[2],3:[2],4:[1]}

# 1 读图
img=cv.imread('C:/Users/polarbear/Desktop/cv/test_card/card3.jpg',1)
img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)


# 2 高斯滤波
img_gray=cv.GaussianBlur(img_gray,(3,3),sigmaX=0,sigmaY=0)
#cv.imshow('tst',img_gray)

# 3 二值化边缘检测
thresh=cv.threshold(img_gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)[1]
threshCnts=cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)[0]

'''
#作出轮廓
crt_img=img.copy()
cv.drawContours(crt_img,threshCnts,-1,[0,0,255],2)
cv.imshow('tst',crt_img)
'''

# 4 找到边缘4顶点 变换裁剪
peri=cv.arcLength(threshCnts[0],True)
approx=cv.approxPolyDP(threshCnts[0],0.02*peri,True)
'''
crt_img=img.copy()
cv.drawContours(crt_img,approx,-1,[0,0,255],3)
cv.imshow('tst',crt_img)
'''
approx=sorted(approx,key=lambda x:x[0][0])

if approx[0][0][1]>=approx[1][0][1]:
    lu_pit=approx[0]
    ld_pit=approx[1]
else:
    lu_pit=approx[1]
    ld_pit=approx[0]
    
if approx[2][0][1]>=approx[3][0][1]:
    ru_pit=approx[2]
    rd_pit=approx[3]
else:
    ru_pit=approx[3]
    rd_pit=approx[2]

# 计算变换矩阵
# 透射变换
(cols,rows)=(300,400)
pts1=np.float32([lu_pit,ld_pit,ru_pit,rd_pit])#透射前位置
pts2=np.float32([[0,400],[0,0],[300,400],[300,0]])#透射后位置
T=cv.getPerspectiveTransform(pts1,pts2)
ret=cv.warpPerspective(img_gray,T,(cols,rows))
# cv.imshow('tst',ret)

# 5 二值化 找轮廓
ret_th=cv.threshold(ret,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)[1]
Cnts=cv.findContours(ret_th,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)[0]
''' 绘制现有轮廓
crt_img=ret.copy()
cv.drawContours(crt_img,Cnts,-1,255,2)
cv.imshow('tst',crt_img)
'''

# 6 删选轮廓
usf_Cnts=[]
for (_,c) in enumerate(Cnts):
    (_,_,w,h)=cv.boundingRect(c)
    if (w>28) & (h>28):
        ar=w/float(h)
        if (ar<1.1) & (ar>0.9):            
            usf_Cnts.append(c)

'''
crt_img=ret.copy()
cv.drawContours(crt_img,usf_Cnts,-1,0,3)
cv.imshow('tst',crt_img)
'''

# 7 建模版计算
(usf_Cnts2,_)=sort_contours(usf_Cnts,method='top2bottom')
ret_img=ret.copy()
answer={}
for m in range(0,5,1):
    (temp_cnts,_)=sort_contours(usf_Cnts2[m*5:m*5+5],method='left2right')
    temp_ans=[]
    for (n,t_cnt) in enumerate(temp_cnts):
        mask=np.zeros(ret.shape,dtype="uint8")
        cv.drawContours(mask,[t_cnt],-1,255,-1)        
        # 比较非零点确定输出
        mask=cv.bitwise_and(ret_th,ret_th,mask=mask)
        total=cv.countNonZero(mask)
        # 输出正确答案位置
        if n in crct_ans[m]:
            cv.drawContours(ret_img,[t_cnt],-1,0,2)        
        if total>550 :
            temp_ans.append(n)
    answer[m]=temp_ans
    
# 8 比较分数
sumgoal=5
getgoal=0
for dt in answer:
    if (answer[dt]==crct_ans[dt]):
        getgoal+=1
goalnum=getgoal/sumgoal*100

outputstr='goal:'+str(goalnum)

font=cv.FONT_HERSHEY_COMPLEX
cv.putText(ret_img,outputstr,[50,50],font,1,0,2,cv.LINE_AA)
cv.imshow('ret',ret_img)   
        

        
    










