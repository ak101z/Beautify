# -*- coding: utf-8 -*-
"""
@author: Akash
"""

import face_recognition
from PIL import Image, ImageDraw

#load the image file
face_image = face_recognition.load_image_file('demo.jpeg')

#get the face landmarks list
face_landmarks_list =  face_recognition.face_landmarks(face_image)

#print the face landmarks list
print(face_landmarks_list)

for face_landmarks in face_landmarks_list:
    #convert the numpy array image into pil image object
    pil_image = Image.fromarray(face_image)
    #convert the pil image to draw object
    d = ImageDraw.Draw(pil_image,"RGBA")
   
    #draw the shapes and fill with color   
    # Add lipstick to top and bottom lips
    # using red polygons and lines filled with red
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)
   

#show the final image    
pil_image.show()

#save the image
#pil_image.save("images/samples/abhi_makeup.jpg")