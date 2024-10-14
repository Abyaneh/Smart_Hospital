# ---- Hemography.py -----
## Perspective image
import cv2
import numpy as np

def air_view(img, coor, x, y, i):
    pts11 = np.float32([coor[i], coor[i+1], coor[i+2], coor[i+3]])
    pts21 = np.float32([[0,0], [0,y], [x,0], [x,y]])
    M = cv2.getPerspectiveTransform(pts11,pts21)
    dst = cv2.warpPerspective(img,M,(x, y))
    return dst