import cv2
import numpy as np

#Carrega uma imagem
imagem = cv2.imread('imagens/estrada.jpeg')
#Recorta a imagem de acordo com o tamanho especificado
recorte = imagem[100:200, 100:200]
#Exibe a imagem recortada
cv2.imshow("Recorte da imagem", recorte)
#Salva no disco
cv2.imwrite("recorte.jpg", recorte)

cv2.waitKey(0)
cv2.destroyAllWindows()
