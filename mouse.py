import cv2 as cv

# Ler a imagem
img = cv.imread('img/baboon.png')

# Mostrar a imagem
cv.imshow('Baboon', img)

# Esperar uma tecla ser pressionada
# Mouse click
def mouse_click(event, x, y, flags, param):

    # Se o botão esquerdo do mouse for pressionado
    if event == cv.EVENT_LBUTTONDOWN:

        # font for left click event
        font = cv.FONT_HERSHEY_SIMPLEX
        LB = 'Left Button Down'

        cv.putText(img, LB, (x, y), font, 1, (255, 255, 0), 2)
        cv.imshow('Baboon', img)
    
    # Se o botão direito do mouse for pressionado
    if event == cv.EVENT_RBUTTONDOWN:
        
          # font for right click event
          font = cv.FONT_HERSHEY_SIMPLEX
          RB = 'Right Button Down'
  
          cv.putText(img, RB, (x, y), font, 1, (255, 255, 0), 2)
          cv.imshow('Baboon', img)

# Mouse move
cv.setMouseCallback('Baboon', mouse_click)

cv.waitKey(0)

# close all windows
cv.destroyAllWindows()
