# -*- encoding: utf-8 -*-
__author__ = "zhangyz"
__date__ = "2017/11/15 0:09"

import cv2 as cv
import numpy as np

def create_image():
    img = np.ones([400, 400, 1], np.uint8)
    img = img * 0
    cv.imshow("new image", img)
    cv.imwrite("d:\\myimages\1.png", img)

create_image()
cv.waitKey(0)
cv.destroyAllWindows()
