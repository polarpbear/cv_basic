# 图像平滑降低噪声


# 均值滤波
''' cv.blur(src,ksize,anchor,borderType)

anchor 默认（-1,-1）均值中心
'''

# 高斯滤波
''' cv.GaussianBlur(src,ksize,sigmax,sigmay,borderType)
去高斯噪声
sigmax sigmay x,y方向标准差
'''

# 中值滤波
'''
cv.medianBlur(src,ksize)
ksize卷积核大小
去高斯噪声
'''











