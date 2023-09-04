# coding=utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagens/atividade_aula11.png',0)

kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(img,kernel,iterations = 1)
erosion = cv2.erode(img,kernel,iterations = 1)
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
plt.title('Imagem')
plt.subplot(222), plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_RGB2BGR))
plt.title('Dilation')
plt.subplot(223), plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_RGB2BGR))
plt.title('Erosion')
plt.subplot(224), plt.imshow(cv2.cvtColor(grad, cv2.COLOR_RGB2BGR))
plt.title('Gradient')

plt.tight_layout()
plt.show()