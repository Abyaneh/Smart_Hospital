import cv2 
import numpy as np
import Aruco
import Hemography
import path


url1 = "http://192.168.82.145:8080/video"
cap1 = cv2.VideoCapture(url1)

url2 = "http://192.168.82.156:8080/video"
cap2 = cv2.VideoCapture(url2)

if cap1.isOpened()==0 and cap2.isOpened()==0:
    print("Cannot open camera")
    exit()


k=0
while True:
    ret1,frame1=cap1.read()
    c1=Aruco.Detect_coordinates(frame1)
    if len(c1)==4:
        k=k+1

    ret2,frame2=cap2.read()
    c2=Aruco.Detect_coordinates(frame2)
    if len(c2)==4:
        k=k+1
    
    if k==2:
        break
    else:
        k=0
cap1.release()
cap2.release()
c2[3][0]=c2[3][0]-200
c2[4][0]=c2[4][0]-200
cap1 = cv2.VideoCapture(url1)
cap2 = cv2.VideoCapture(url2)

i=0
j=0
while True:
    if i==0:
        ret,cam=cap1.read()
        frame= Hemography.air_view(cam, c1, 520, 590, 1)
        
        
    elif i==1:
        ret,cam=cap2.read()
        frame=Hemography.air_view(cam, c2, 720, 590, 3)
        
    
    
     
    
    frame01, Cx, Cy= Aruco.aruco_detection(frame)
    if i==0:
        frame01=path.First_areas(frame01, 90)
    elif i==1:
        frame01=path.last_area(frame01, 90, 100)
    cv2.imshow('Camera', frame01)
    print(f'({Cx},{Cy})')
    #Cx, Cy=center[0], center[1]
    if Cx>480 and j==0:
        ret,frame=cap2.read()
        i=1
        j=j+1
        cap1.release()
        cv2.destroyAllWindows()
        

    if cv2.waitKey(1)==27:
        break
        
