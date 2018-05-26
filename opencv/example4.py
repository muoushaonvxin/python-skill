# -*- encoding: utf-8 -*-
__author__ = "zhangyz"
__date__ = "2017/11/30 22:32"

import cv2 as cv

def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo",  dst)

def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)

def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)

def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


src1 = cv.imread("I:/natuto/20110909184340f9ec8.jpg")
src2 = cv.imread("I:/natuto/game_manwall_303057_m.jpg")
print(src1.shape)
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)

add_demo(src1, src2)
cv.waitKey(0)

cv.destroyAllWindows()