import cv2
#Carrega a imagem
img = cv2.imread('imagens/original.jpeg')
#Ajusta o tamanho da imagem
img = cv2.resize(img,(350, 505))
#Converte pro sistema de cores HSV
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Faz uma cópia do arquivo e atribui a variável gray
gray = img.copy()
#Pega o tamanho das linhas e colunas
(row, col) = img.shape[0:2]
#Percorre linhas e colunas
for i in range(row):
    for j in range(col):
        #Percorre a imagem pixel a pixel e altera o valor do pixel de acordo com a condição IF
        if(hsv[i,j][0]<170) or (hsv[i, j][0]>200):
            gray[i, j] = sum(img[i, j])*0.33

#Exibe a imagem original
cv2.imshow('Original', img)
#Exibe a imagem no canal de cores HSV
cv2.imshow('Hsv', hsv)
#Exibe a imagem em escala de cinza
cv2.imshow('Merge', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
