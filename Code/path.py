# ---- Path.py -----
# Path_drawing
import cv2

def First_areas(img,a):
    shape_img=img.shape
    width=shape_img[0]
    length=shape_img[1]

    c_width=round(width/2)

    start1=(0, c_width+round(a/2))
    end1=(length, c_width+round(a/2))

    start2=(0, c_width-round(a/2))
    end2=(length, c_width-round(a/2))

    cv2.line(img, start1, end1, (0, 255, 0), 2)
    cv2.line(img, start2, end2, (0, 255, 0), 2)
    
    return(img)


def last_area(img, a, x):
    shape_img=img.shape
    width=shape_img[0]
    length=shape_img[1]

    c_width=round(width/2)

    #line
    start1=(0, c_width+round(a/2))
    end1=(x, c_width+round(a/2))

    start2=(0, c_width-round(a/2))
    end2=(x, c_width-round(a/2))  

    cv2.line(img, start1, end1, (0, 255, 0), 2)
    cv2.line(img, start2, end2, (0, 255, 0), 2)

    #quarter circle
    radius1=(c_width-round(a/2), c_width-round(a/2))
    radius2=(c_width+round(a/2), c_width+round(a/2))
    center= (x,0)
    cv2.ellipse(img, center, radius1, 0, 0, 90, (0, 255, 0), 2)
    cv2.ellipse(img, center, radius2, 0, 0, 90, (0, 255, 0), 2)
    return(img)


