import cv2 as cv
import numpy as np

img = cv.imread('img/pikachu.png')

imgEq = cv.equalizeHist(cv.imread('img/pikachu.png', 0))

cv.imshow('Original', img)

cv.imshow('Equalizada', imgEq)

k = cv.waitKey(0)
