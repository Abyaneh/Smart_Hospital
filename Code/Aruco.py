# ---- Aruco.py -----
# Aruco_detection
import cv2
from cv2 import aruco
import numpy as np


def aruco_detection(img):
    global topLeft, topRight, bottomRight, bottomLeft, cX, cY
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Change grayscale
    parameters = cv2.aruco.DetectorParameters_create()  # Marker detection parameters
    corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, aruco_dict,
                                                                parameters=parameters)
    if len(corners) > 0:
        # flatten the ArUco IDs list
        ids = ids.flatten()
        # loop over the detected ArUCo corners
        for (markerCorner, markerID) in zip(corners, ids):
            # extract the marker corners (which are always returned in
            # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
            # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            
        cv2.line(img, topLeft, topRight, (0, 255, 0), 2)
        cv2.line(img, topRight, bottomRight, (0, 255, 0), 2)
        cv2.line(img, bottomRight, bottomLeft, (0, 255, 0), 2)
        cv2.line(img, bottomLeft, topLeft, (0, 255, 0), 2)
        cX = int((topLeft[0] + bottomRight[0]) / 2.0)
        cY = int((topLeft[1] + bottomRight[1]) / 2.0)
        cv2.circle(img, (cX, cY), 4, (0, 0, 255), -1) 
        cv2.putText(img, f'Center:({cX},{cY})',
                (topLeft[0], topLeft[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 2)
    
    
    
    
    return img, cX, cY


def Detect_coordinates(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()
    
    corners, ids, rejected_img_points = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    

    marker_centers = {}
    for i in range(len(ids)):
        marker_id = ids[i][0]
        center = np.mean(corners[i][0], axis=0).astype(int)
        marker_centers[marker_id] = center
        #print(f"Marker ID: {marker_id}, Center Coordinates: {center}")


        cv2.circle(image, tuple(center), 5, (0, 0, 255), -1)
    

    return marker_centers
    