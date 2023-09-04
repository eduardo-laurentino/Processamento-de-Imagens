import cv2
import numpy as np
#Carrega a imagem
img = cv2.imread('imagens/noise.jpg')

#Aplica medianBlur onde o elemento central da imagem é substituído pela mediana de todos os pixels na área do kernel
median = cv2.medianBlur(img, 7)

#Carrega a imagem original e a imagem depois de aplicado medianBlur
cv2.imshow('Img.jpg', img)
cv2.imshow('Median.jpg', median)

cv2.waitKey(0)
cv2.destroyAllWindows()
