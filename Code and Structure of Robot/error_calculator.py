# ---- error.py -----
# error_calculating
import numpy as np


def err1(Cy_robot,img):

    shape_img=img.shape
    Cy=shape_img[0]/2
    return Cy_robot-Cy

def err2(Cy_robot, Cx_robot, img, x):
    shape_img=img.shape
    Cy=shape_img[0]/2
    radius=round(shape_img[0]/2)

    if x >= Cx_robot:
        return Cy_robot-Cy
    else:
        xc, yc = (x, 0)
        return np.sqrt((Cx_robot - xc)**2 + (Cy_robot - yc)**2) - radius
        