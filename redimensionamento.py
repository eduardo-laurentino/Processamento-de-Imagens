import cv2
import numpy as np

#Carrega a imagem
img = cv2.imread('imagens/estrada.jpeg')
#Exibe a imagem original
cv2.imshow("Original", img)
#Pega a largura e atribui a variável largura
largura = img.shape[1]
#Pega a altura e atribui a variável altura
altura = img.shape[0]
#Pega a proporção entre a largura e a altura
proporcao = float(altura / largura)
largura_nova = 320 #em pixels
#Define a nov altura da imagem
altura_nova = int(largura_nova * proporcao)
#Redimensiona a imagem
tamanho_novo = (largura_nova, altura_nova)
img_redimensionada = cv2.resize(img, tamanho_novo, interpolation=cv2.INTER_AREA)
#Exibe a imagem redimensionada
cv2.imshow("Resutado", img_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
