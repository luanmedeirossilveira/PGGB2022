import numpy as np
import cv2 as cv
import sys

# Variaveis globais
backgroundName = sys.argv[1]
hasCam = sys.argv[2]
background = cv.imread('img/' + backgroundName)
background = cv.resize(background, (400, 400), None, .25, .25)
capture = cv.VideoCapture(0)
palette = cv.imread('img/palette.png')
palette = cv.resize(palette, (400, 131), None, .25, .25)
stickers = {
  'juiz': cv.imread('img/juiz.png', cv.IMREAD_UNCHANGED),
  'pistola': cv.imread('img/pistola.png', cv.IMREAD_UNCHANGED),
  'world': cv.imread('img/world.png', cv.IMREAD_UNCHANGED),
  'boots': cv.imread('img/boots.png', cv.IMREAD_UNCHANGED),
  'ball': cv.imread('img/bal.png', cv.IMREAD_UNCHANGED),
}
kernel = np.ones((5,5),np.uint8)

# Função de Overlay
def overlay(background, foreground, x_offset=None, y_offset=None):
    bg_h, bg_w, bg_channels = background.shape
    fg_h, fg_w, fg_channels = foreground.shape

    assert bg_channels == 3, f'background image should have exactly 3 channels (RGB). found:{bg_channels}'
    assert fg_channels == 4, f'foreground image should have exactly 4 channels (RGBA). found:{fg_channels}'

    # center by default
    if x_offset is None: x_offset = (bg_w - fg_w) // 2
    if y_offset is None: y_offset = (bg_h - fg_h) // 2

    w = min(fg_w, bg_w, fg_w + x_offset, bg_w - x_offset)
    h = min(fg_h, bg_h, fg_h + y_offset, bg_h - y_offset)

    if w < 1 or h < 1: return

    # clip foreground and background images to the overlapping regions
    bg_x = max(0, x_offset)
    bg_y = max(0, y_offset)
    fg_x = max(0, x_offset * -1)
    fg_y = max(0, y_offset * -1)
    foreground = foreground[fg_y:fg_y + h, fg_x:fg_x + w]
    background_subsection = background[bg_y:bg_y + h, bg_x:bg_x + w]

    # separate alpha and color channels from the foreground image
    foreground_colors = foreground[:, :, :3]
    alpha_channel = foreground[:, :, 3] / 255  # 0-255 => 0.0-1.0

    # construct an alpha_mask that matches the image shape
    alpha_mask = np.dstack((alpha_channel, alpha_channel, alpha_channel))

    # combine the background with the overlay image weighted by alpha
    composite = background_subsection * (1 - alpha_mask) + foreground_colors * alpha_mask

    # overwrite the section of the background image that has been updated
    background[bg_y:bg_y + h, bg_x:bg_x + w] = composite
    out = background.copy()
    return out

# Verificar se será usado a webcam
if hasCam == 'True':
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

# Senão, será usado a imagem
else:
  # Mostrar a imagem
  numpy_vertical = np.vstack((palette, background))
  cv.imshow('Editor de Imagem', numpy_vertical)

  def mouse_click_editor(event, x, y, flags, param):
    global sticker
    global out

    # Se o botão esquerdo do mouse for pressionado
    if event == cv.EVENT_RBUTTONDOWN:
      if (x >= 0 and x <= 48) and (y >= 0 and y <= 50):
        sticker = stickers['juiz']

      elif (x >= 73 and x <= 121) and (y >= 0 and y <= 50):
        sticker = stickers['pistola']

      elif (x >= 164 and x <= 206) and (y >= 0 and y <= 50):
        sticker = stickers['world']

      elif (x >= 251 and x <= 301) and (y >= 0 and y <= 50):
        sticker = stickers['boots']

      elif (x >= 348 and x <= 397) and (y >= 0 and y <= 50):
        sticker = stickers['ball']

      # Dilation
      elif (x >= 21 and x <= 94) and (y >= 60 and y <= 75):
        imgDilation = cv.dilate(background,kernel,iterations = 1)
        numpy_vertical = np.vstack((palette, imgDilation))
        cv.imshow('Editor de Imagem', numpy_vertical)
      
      # Binarização
      elif (x >= 104 and x <= 190) and (y >= 60 and y <= 75):
        ret,thresh1 = cv.threshold(background, 127, 255, cv.THRESH_BINARY)
        numpy_vertical = np.vstack((palette, thresh1))
        cv.imshow('Editor de Imagem', numpy_vertical)

      # Blur
      elif (x >= 200 and x <= 240) and (y >= 60 and y <= 75):
        imgBlurred5x5 = cv.blur(background, (5, 5))
        numpy_vertical = np.vstack((palette, imgBlurred5x5))
        cv.imshow('Editor de Imagem', numpy_vertical)
      
      # Gaussian
      elif (x >= 249 and x <= 317) and (y >= 60 and y <= 75):
        imgGaussian5x5 = cv.GaussianBlur(background, (5, 5), 0)
        numpy_vertical = np.vstack((palette, imgGaussian5x5))
        cv.imshow('Editor de Imagem', numpy_vertical)

      # Median
      elif (x >= 325 and x <= 380) and (y >= 60 and y <= 75):
        imgMedian5x5 = cv.medianBlur(background, 5)
        numpy_vertical = np.vstack((palette, imgMedian5x5))
        cv.imshow('Editor de Imagem', numpy_vertical)
      
      # Bilateral
      elif (x >= 21 and x <= 94) and (y >= 85 and y <= 100):
        imgBilateral5x5 = cv.bilateralFilter(background, 9, 75, 75)
        numpy_vertical = np.vstack((palette, imgBilateral5x5))
        cv.imshow('Editor de Imagem', numpy_vertical)

      # Canny
      elif (x >= 104 and x <= 190) and (y >= 85 and y <= 100):
        imgCanny1 = cv.Canny(background, 100, 200)
        numpy_vertical = np.vstack((palette, imgCanny1))
        cv.imshow('Editor de Imagem', numpy_vertical)
      
      # Sobel
      elif (x >= 200 and x <= 240) and (y >= 85 and y <= 100):
        imgSobel = cv.Sobel(background, cv.CV_64F, 1, 0, ksize=5)
        numpy_vertical = np.vstack((palette, imgSobel))
        cv.imshow('Editor de Imagem', numpy_vertical)
      
      # Erosion
      elif (x >= 249 and x <= 317) and (y >= 85 and y <= 100):
        imgLaplacian = cv.Laplacian(background, cv.CV_64F)
        numpy_vertical = np.vstack((palette, imgLaplacian))
        cv.imshow('Editor de Imagem', numpy_vertical)
      
      # Laplacian
      elif (x >= 325 and x <= 380) and (y >= 85 and y <= 100):
        imgErosion = cv.erode(background,kernel,iterations = 1)
        numpy_vertical = np.vstack((palette, imgErosion))
        cv.imshow('Editor de Imagem', numpy_vertical)

      elif (x >= 337 and x <= 391) and (y >= 114 and y <= 130):
        numpy_vertical = np.vstack((palette, background))
        cv.imshow('Editor de Imagem', numpy_vertical)

    # Se o botão esquerdo do mouse for pressionado
    if event == cv.EVENT_LBUTTONDOWN:
      out = overlay(background, sticker, x, y) 
      out = cv.resize(out, (400, 400), None, .25, .25)
      numpy_vertical = np.vstack((palette, out))
      cv.imshow('Editor de Imagem', numpy_vertical)

  # Mouse move
  cv.setMouseCallback('Editor de Imagem', mouse_click_editor)

  cv.waitKey(0)
