import cv2
import numpy as np
imagem = cv2.imread('imagens/estrada.jpeg')
img_modificada = cv2.imread('imagens/estrada.jpeg')
imagem = cv2.resize(imagem,(450, 505))#redefine as dimensões da imagem.
(b, g, r) = imagem[0, 0]#separa os canais da imagem na coordenadda (0,0).
print("Largura em pixels: ", imagem.shape[1])#retorna a largura da imagem.
print("Altura em pixels: ", imagem.shape[0])#retorna a altura da imagem.
print("Quantidade de canais: ", imagem.shape[2])#retorna a quantidade de canais da imagem.
print("O pixel (0,0) tem as seguintes cores: ", 'Vermelho:', r, 'Verde:', g, 'Azul:', b)
cv2.imshow("Original", imagem)#mostra a imagem na tela.

#percorrendo uma imagem pixel a pixel com dois laços for e mudando a cor.
for x in range(0, imagem.shape[0], 10):#percorre linhas
    for y in range(0, imagem.shape[1], 10):#percorre colunas
        imagem[x:x+3, y:y+3] = (0, 255, 255)# desenha pixels 3x3  em toda imagem pulando de 10 em 10 pixels nas linhas e colunas.
cv2.imshow("Imagem Modificada", imagem)

# fatiamento e desenho sobre a imagem

#cria um retangulo azul por toda a largura da imagem.
img_modificada[30:50,:] = (255, 0, 0)

#cria um quadrado vermelho.
img_modificada[30:150, 50:100] = (0, 0, 255)

#cria um retangulo verde da linha 150 a 300 nas colunas 250 a 350.
img_modificada[:,200:350] = (0, 255, 0)

#cria um quadrado ciano da linha 150 a 300 nas colunas 250 a 350
img_modificada[300:400, 50:150] = (255, 255, 0)

#cria um quadrado branco 
img_modificada[250:350, 300:400] = (255, 255, 255)

#cria um quadrado preto
img_modificada[70:100, 300:450] = (0, 0, 0)

#escrevendo em imagens
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_modificada, 'OpenCV', (350, 230), fonte, 2,  (255, 255, 255), 2, cv2.LINE_AA)
vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)
cv2.line(img_modificada, (0, 0), (100, 200), verde, 5)
cv2.line(img_modificada, (300, 200), (150, 150), vermelho, 5)
cv2.rectangle(img_modificada, (20, 20), (120, 120), azul, 10)
cv2.rectangle(img_modificada, (200, 50),(225, 125), verde, -1)
(x, y) = (img_modificada.shape[1] // 2 , img_modificada.shape[0] // 2)
for raio in range(0, 175, 15):
    cv2.circle(img_modificada, (x, y), raio, vermelho)

cv2.imshow("Desenho sobre a imagem", img_modificada)

cv2.waitKey(0)#espera pressionar qualquer tecla e fecha a janela.
cv2.destroyAllWindows()#destroi todas as janelas depois que forem fechadas
#cv2.imwrite("IMG salva.jpeg", imagem)#salva a imagem
