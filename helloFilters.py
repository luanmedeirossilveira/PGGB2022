import numpy as np
import cv2 as cv

# original
img = cv.imread('pikachu.png')

imgGrayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret,thresh1 = cv.threshold(imgGrayscale, 127, 255, cv.THRESH_BINARY)

cv.imshow('Original', img)
cv.imshow('Grayscale', imgGrayscale)
cv.imshow('Binarização', thresh1)

k = cv.waitKey(0)