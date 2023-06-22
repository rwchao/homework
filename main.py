import cv2
import numpy as np
from matplotlib import pyplot as plt


def detect_circles(image):
    dst = cv2.pyrMeanShiftFiltering(image,10,1000)#消除噪声！！！！必不可少
    cimage = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(cimage,cv2.HOUGH_GRADIENT,1,1000,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(image,(i[0],i[1]),i[2],(0,0,255),2)
        cv2.circle(image,(i[0],i[1]),2,(255,0,0),2)#圆心
    cv2.imshow("circles",image)


src = cv2.imread(r"/Users/yiyue/Downloads/6.jpg")
cv2.imshow("image",src)
cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)
detect_circles(src)
cv2.waitKey(0)
cv2.destroyAllWindows()
