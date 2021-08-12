import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# meanshift 图片追踪
'''
cv.meanShift(probImage,window,criteria)

probImage ROI区域，目标直方图反向投影
window 初始搜索窗口
criteria 停止搜索的准则，迭代次数的最大值或窗口中心偏移的最大值

'''
# Camshift 图像追踪
'''
可对搜索窗口大小进行调整，以适应目标位置大小变化
先用meanshift计算，然后计算最佳拟合椭圆方向
cv.CamShift(probImage,window,criteria)
'''



# 1 获取图像
cap=cv.VideoCapture('tst_track.mp4')
 
# 2 获取第一帧 指定目标位置
ret,frame=cap.read()

# 目标位置行高列宽 (974,500) (1053,717)
r,h,c,w=500,217,974,79

track_window=(c,r,w,h)

roi=frame[r:r+h,c:c+w] # 目标区域图像

# 3 计算直方图
# 转换为HSV空间
hsv_roi=cv.cvtColor(roi,cv.COLOR_BGR2HSV)

# 计算直方图
roi_hist=cv.calcHist([hsv_roi],[0],None,[180],[0,180])
# 归一化
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)

# 4 目标追踪
term_crit=(cv.TERM_CRITERIA_EPS|cv.TERM_CRITERIA_COUNT,20,1)
#最大迭代次数，最小位移距离

while(True):
    # 获取每一帧图像
    ret,frame=cap.read()
    if ret==True:
        # 计算直方图反向投影
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        dst=cv.calcBackProject([hsv],[0],roi_hist,[0,100],1)

        # 进行meanshift追踪
        '''
        ret2,track_window=cv.meanShift(dst,track_window,term_crit)
        # 在图上显示
        x,y,w,h=track_window
        img2=cv.rectangle(frame,(x,y),(x+w,y+h),[0,0,255],2)
        

        # 进行Camshift追踪
        '''
        ret2,track_window=cv.CamShift(dst,track_window,term_crit)
        pts=cv.boxPoints(ret2)
        pts=np.int0(pts)
        img2=cv.polylines(frame,[pts],True,[0,0,255],2)        
       
        cv.namedWindow('track',cv.WINDOW_NORMAL)
        cv.imshow('track',img2)
        
        if cv.waitKey(60) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()







































