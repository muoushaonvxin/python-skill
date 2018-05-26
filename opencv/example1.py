# -*- encoding: utf-8 -*-
__author__ = "zhangyz"
__date__ = "2017/11/12 2:21"

import cv2

src = cv2.imread("I:/natuto/sasuke.jpg")
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input image", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Hi python!")
