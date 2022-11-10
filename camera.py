import numpy as np
import cv2 as cv

capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Cannot open camera")
    exit(0)

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    cv.imshow('frame', frame)

capture.release()
cv.destroyAllWindows()
