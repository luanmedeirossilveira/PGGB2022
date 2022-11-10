import numpy as np
import cv2 as cv

# Original
img = cv.imread('img/pikachu.png')

# Original com flag=0
img0 = cv.imread('img/pikachu.png', 0)

kernel = np.ones((5,5),np.uint8)

# Grayscale
imgGrayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Binarização
ret,thresh1 = cv.threshold(imgGrayscale, 127, 255, cv.THRESH_BINARY)

# Binarização Dark
ret,threshDark = cv.threshold(imgGrayscale, 200, 255, cv.THRESH_BINARY)

# Binarização Invert
ret,threshInvert = cv.threshold(imgGrayscale, 127, 255, cv.THRESH_BINARY_INV)

# Blur 5x5
imgBlurred5x5 = cv.blur(imgGrayscale, (5, 5))

# Blur 15x15
imgBlurred15x15 = cv.blur(imgGrayscale, (15, 15))

# Gaussian 5x5
imgGaussian5x5 = cv.GaussianBlur(imgGrayscale, (5, 5), 0)

# Gaussian 15x15
imgGaussian15x15 = cv.GaussianBlur(imgGrayscale, (15, 15), 0)

# Median 5x5
imgMedian5x5 = cv.medianBlur(imgGrayscale, 5)

# Median 15x15
imgMedian15x15 = cv.medianBlur(imgGrayscale, 15)

# Bilateral 5x5
imgBilateral5x5 = cv.bilateralFilter(imgGrayscale, 9, 75, 75)

# Bilateral 15x15
imgBilateral15x15 = cv.bilateralFilter(imgGrayscale, 9, 75, 75)

# Canny 1
imgCanny1 = cv.Canny(imgGrayscale, 100, 200)

# Canny 2
imgCanny2 = cv.Canny(imgBlurred5x5, 100, 200)

# Canny 3
imgCanny3 = cv.Canny(imgBlurred15x15, 100, 200)

# Sobel
imgSobel = cv.Sobel(imgGrayscale, cv.CV_64F, 1, 0, ksize=5)

# Laplacian
imgLaplacian = cv.Laplacian(imgGrayscale, cv.CV_64F)

# Laplacian 2
imgLaplacian2 = cv.Laplacian(imgGrayscale, cv.CV_64F, ksize=5)

# Laplacian 3
imgLaplacian3 = cv.Laplacian(imgGrayscale, cv.CV_64F, ksize=15)

# Erosion
imgErosion = cv.erode(imgGrayscale,kernel,iterations = 1)

# Dilation
imgDilation = cv.dilate(imgGrayscale,kernel,iterations = 1)

# Opening
imgOpening = cv.morphologyEx(imgGrayscale, cv.MORPH_OPEN, kernel)

# Closing
imgClosing = cv.morphologyEx(imgGrayscale, cv.MORPH_CLOSE, kernel)

# Morphological Gradient
imgMorphGradient = cv.morphologyEx(imgGrayscale, cv.MORPH_GRADIENT, kernel)

# Top Hat
imgTopHat = cv.morphologyEx(imgGrayscale, cv.MORPH_TOPHAT, kernel)

# Black Hat
imgBlackHat = cv.morphologyEx(imgGrayscale, cv.MORPH_BLACKHAT, kernel)

# cv.imshow('Original', img)
# cv.imshow('Original com 0', img0)
# cv.imshow('Grayscale', imgGrayscale)
# cv.imshow('Binarização', thresh1)
# cv.imshow('Binarização 2', threshDark)
# cv.imshow('Binarização Invert', threshInvert)
# cv.imshow('Blur 5x5', imgBlurred5x5)
# cv.imshow('Blur 15x15', imgBlurred15x15)
# cv.imshow('Gaussian 5x5', imgGaussian5x5)
# cv.imshow('Gaussian 15x15', imgGaussian15x15)
# cv.imshow('Median 5x5', imgMedian5x5)
# cv.imshow('Median 15x15', imgMedian15x15)
# cv.imshow('Bilateral 5x5', imgBilateral5x5)
# cv.imshow('Bilateral 15x15', imgBilateral15x15)
# cv.imshow('Canny 1', imgCanny1)
# cv.imshow('Canny 2', imgCanny2)
# cv.imshow('Canny 3', imgCanny3)
# cv.imshow('Sobel', imgSobel)
# cv.imshow('Laplacian', imgLaplacian)
# cv.imshow('Laplacian 2', imgLaplacian2)
# cv.imshow('Laplacian 3', imgLaplacian3)
# cv.imshow('Erosion', imgErosion)
# cv.imshow('Dilation', imgDilation)
# cv.imshow('Opening', imgOpening)
# cv.imshow('Closing', imgClosing)
# cv.imshow('Morphological Gradient', imgMorphGradient)
# cv.imshow('Top Hat', imgTopHat)
cv.imshow('Black Hat', imgBlackHat)

k = cv.waitKey(0)