import numpy as np
import cv2 as cv

img = cv.imread('img/bolinhas.png')

imgGrayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

b,g,r = cv.split(img)

imgB = cv.cvtColor(b, cv.COLOR_GRAY2BGR)
imgG = cv.cvtColor(g, cv.COLOR_GRAY2BGR)
imgR = cv.cvtColor(r, cv.COLOR_GRAY2BGR)

imgB = cv.merge((b, np.zeros_like(b), np.zeros_like(b)))

imgG = cv.merge((np.zeros_like(g), g, np.zeros_like(g)))

imgR = cv.merge((np.zeros_like(r), np.zeros_like(r), r))

cv.imshow('Original', img)
cv.imshow('Grayscale', imgGrayscale)
cv.imshow('B', imgB)
cv.imshow('G', imgG)
cv.imshow('R', imgR)

k = cv.waitKey(0)
