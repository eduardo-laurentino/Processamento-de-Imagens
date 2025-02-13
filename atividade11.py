"""Esse código aplica operações morfológicas a uma imagem em escala de cinza, usando técnicas como erosão e dilatação . Ele manipula a estrutura da imagem para destacar ou remover características específicas"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagens/atividade_aula11.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(200,200), interpolation = cv2.INTER_CUBIC)

k_erosion = np.ones((3,3), dtype = np.uint8)

eroded = cv2.erode(img, k_erosion, anchor=(2,2), iterations=9)

k_erosion = np.ones((51,41), dtype = np.uint8)

eroded_tmp = cv2.erode(img, k_erosion)

k_dilation = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(31,31))

dilated = cv2.dilate(eroded_tmp, k_dilation)

k_dilation = np.ones((9,9), dtype = np.uint8)

dilated_tmpx = cv2.dilate(img, k_dilation, iterations=5)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))

eroded_tmpx = cv2.erode(dilated_tmpx, kernel, iterations=5)

rounded = cv2.dilate(eroded_tmpx, kernel, iterations=3)

kernel1 = np.array([ [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,0],
                     [1,1,1,1,1,1,0],
                     [1,1,1,1,1,1,0],],dtype = np.uint8)
img2 = cv2.erode(img, kernel1, iterations=3)

kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT,(18,27))
img3 = cv2.erode(rounded, kernel3, iterations=3)
img4 = cv2.dilate(img3, kernel3, iterations=1)

plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Img')
plt.subplot(222), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('Img2')
plt.subplot(223), plt.imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))
plt.title('Img3')
plt.subplot(224), plt.imshow(cv2.cvtColor(rounded, cv2.COLOR_BGR2RGB))
plt.title('Img4')

plt.tight_layout()
plt.show()