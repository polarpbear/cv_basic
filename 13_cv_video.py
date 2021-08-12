# 视频读取

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 创建读取视频对象
'''
cap=cv.VideoCapture(filepath)
文件路径
'''

# 视频属性信息
'''
retval=cap.get(propId)

0 cv2.CAP_PROP_POS_MESC  当前位置(ms)
1 cv2.CAP_PROP_POS_FRAMES 从0开始索引帧位置
2 cv2.CAP_PROP_POS_AVI_RATIO 视频相对位置(0开始,1结束)
3 cv2.CAP_PROP_FRAME_WIDTH 视频流帧宽度 像素
4 cv2.CAP_PROP_FRAME_HEIGHT 视频流帧高度 像素
5 cv2.CAP_PROP_FPS 帧率 50Hz，60Hz
6 cv2.CAP_PROP_FOURCC 编辑器四字符代码 AVI,RMVB等编码方式
7 cv2.CAP_PROP_FRAME_COUNT 视频文件帧数
'''
# 修改视频信息
'''
cap.set(propId,value)

value: 修改后的属性值
'''

# 判断读取是否成功
'''
cap.isOpened

True False
'''
# 获取视频的一帧图像
'''
ret,frame=cap.read()

ret True False
frame 读取的图像

'''

# 视频释放
'''
cap.release()
'''


cap=cv.VideoCapture('C:/Users/polarbear/Desktop/cv/0094.MOV')

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret ==True:
        cv.imshow('frame',frame)
    if cv.waitKey(25) & 0xFF ==ord('q'):
        break

cap.release()
cv.destroyAllWindows()

















