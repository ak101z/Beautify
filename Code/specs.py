import cv2
from PIL import Image
import sys
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

sunglasses_img = cv2.imread("specs2.jpg")
image = cv2.imread('face2.jpg') # input.jpeg
#cv2.imshow("sunglass",sunglasses_img)
cv2.imshow("Original",image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
centers = []
for (x,y,w,h) in faces:
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = image[y:y+h,x:x+w]
    eyes = eyes_cascade.detectMultiScale(roi_gray, 1.3, 5)
    for (e_x,e_y,e_w,e_h) in eyes:
        centers.append((x + int(e_x + 0.5*e_w),y + int(e_y + 0.5*e_h)))
if len(centers) > 1 :
    h,w = sunglasses_img.shape[:2]
    eye_distance = abs(centers[1][0] - centers[0][0])
    sunglasses_width = 2.12 * eye_distance
    scaling_factor = sunglasses_width / w
    #print(scaling_factor,eye_distance)
    overlay_sunglasses = cv2.resize(sunglasses_img,None,fx=scaling_factor,fy=scaling_factor,
                                    interpolation=cv2.INTER_AREA)
    x = centers[0][0] if centers[0][0] < centers[1][0] else centers[1][0]
    x-= int(0.26*overlay_sunglasses.shape[1]) 
    y+= int(0.04*overlay_sunglasses.shape[0])
    h,w=overlay_sunglasses.shape[:2]
    h,w=int(h),int(w)
    frame_roi = image[y:y+h,x:x+w]
    gray_overlay_sunglasses = cv2.cvtColor(overlay_sunglasses,cv2.COLOR_BGR2GRAY)
    ret,mask=cv2.threshold(gray_overlay_sunglasses,180,255,cv2.THRESH_BINARY_INV)
    mask_inv = cv2.bitwise_not(mask)
    try:
        masked_face = cv2.bitwise_and(overlay_sunglasses,overlay_sunglasses,mask=mask)
        masked_frame = cv2.bitwise_and(frame_roi,frame_roi,mask=mask_inv)
    except cv2.error as e:
        print("ignoring arithmatic exception")
    image[y:y+h,x:x+w] = cv2.add(masked_face,masked_frame)
else:
    print("eyes not detected")
cv2.imshow("final",image)
cv2.waitKey(0)#added this
