# coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('imagens/if-caxias-logo.png')
mask = cv2.imread('imagens/if-caxias-mask.png',0)
cv2.imshow('Original', img)
rows, cols = mask.shape
roi = img[0:rows, 0:cols]

telea = cv2.inpaint(roi,mask,3,cv2.INPAINT_TELEA)
img[0:rows, 0:cols]=telea
cv2.imshow('Telea', img)

ns = cv2.inpaint(roi,mask,3,cv2.INPAINT_NS)
img[0:rows, 0:cols]=ns
cv2.imshow('Ns', img)

cv2.waitKey(0)
cv2.destroyAllWindows()