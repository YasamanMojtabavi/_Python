import cv2
import numpy as np

my_image_1=cv2.imread("D:\python\image_processing\project/2.jpg")
my_image_2=cv2.imread("D:\python\image_processing\project/1.jpg")

my_image_1=cv2.cvtColor(my_image_1,cv2.COLOR_BGR2GRAY)
my_image_2=cv2.cvtColor(my_image_2,cv2.COLOR_BGR2GRAY)
         
_,image_1 =cv2.threshold(my_image_1,100,255,cv2.THRESH_BINARY)       
_,image_2 =cv2.threshold(my_image_2,100,255,cv2.THRESH_BINARY)

result=image_2 - image_1

cv2.imshow("",result)
cv2.waitKey()