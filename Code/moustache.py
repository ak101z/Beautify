## this script adds a brown moustache to all detected faces in a photograph!
## Using Haar Cascade Classifier
## @author :- Kunal Gupta ( cite as kg777)

import cv2
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"  # for face detection
faceCascade = cv2.CascadeClassifier(cascPath)

mst = cv2.imread('moustache.png')

def put_moustache(mst,fc,x,y,w,h):
    
    face_width = w
    face_height = h

    mst_width = int(face_width*0.4466666)
    mst_height = int(face_height*0.142857)

    mst = cv2.resize(mst,(mst_width,mst_height))

    for i in range(int(0.62857142857*face_height),int(0.62857142857*face_height)+mst_height):
        for j in range(int(0.29166666666*face_width),int(0.29166666666*face_width)+mst_width):
            for k in range(3):
                if mst[i-int(0.62857142857*face_height)][j-int(0.29166666666*face_width)][k] <235:
                    fc[y+i][x+j][k] = mst[i-int(0.62857142857*face_height)][j-int(0.29166666666*face_width)][k]
    
    return fc

source_image_path = 'iliev_alexander.jpg'  ## input.jpeg FF.png puja2.jpg Add the image name here
SRC = cv2.imread(source_image_path)
gray = cv2.cvtColor(SRC, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Face!!',SRC)
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

for (x, y, w, h) in faces:
        #cv2.rectangle(SRC, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        SRC = put_moustache(mst,SRC,x,y,w,h)
cv2.imshow('Moustache Face!!',SRC)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
