#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:43:13 2020

@author: akashmane
"""

# Enter your code here
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib


def calcVariance(patch):
    x = cv2.Scharr(patch, -1, 1, 0)
    y = cv2.Scharr(patch, -1, 0, 1)
    return np.abs(x) + np.abs(y)


def getPatch(xy, img):
    patch = img[xy[1] - 15:xy[1] + 15, xy[0] - 15:xy[0] + 15]
    return patch

def pickBestAround(xy, image):
    bestV = 0
    best_xy = None
    for move in np.array([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]) * 30:      
        xy_m = xy + move
        patch = getPatch(xy_m, image)
        variance = 1/calcVariance(patch).sum()
        if variance > bestV:
            bestV = variance
            best_xy = xy_m

        return getPatch(best_xy, image)

def onMouse(action, x, y, flags, img):
    if action == cv2.EVENT_LBUTTONDOWN or action == cv2.EVENT_RBUTTONDOWN:
        colorPatch = pickBestAround((x, y), img)
        cv2.seamlessClone(
            colorPatch, img, colorPatch, (x, y), cv2.NORMAL_CLONE, blend=img)



img = cv2.imread("image.png", 1)
# Make a dummy image, will be useful to clear the drawing
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", onMouse, img)

k = 0
while k != 27:
    cv2.imshow("Window", img)
    k = cv2.waitKey(20)

cv2.destroyAllWindows()