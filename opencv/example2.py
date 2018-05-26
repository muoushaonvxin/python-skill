# -*- encoding: utf-8 -*-
__author__ = "zhangyz"
__date__ = "2017/11/13 23:13"

import cv2 as cv
import numpy as np

# 查看图片的属性和大小
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)

src = cv.imread("I:/natuto/sasuke.jpg")
get_image_info(src)

# 查看视频的帧数, 调用本地摄像头
def get_video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break

get_video_demo()

# 把一张图片保存成为另外一张图片
src = cv.imread("I:/natuto/sasuke.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
gray =cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("I:/natuto/sasuke000001.png", gray)