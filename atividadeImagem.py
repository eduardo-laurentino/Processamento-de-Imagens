import cv2 
import random
  
#Carrega uma imagem
img = cv2.imread('imagens/image.jpg')
#Exibe a imagem na tela
cv2.imshow('image', img) 

#Define cores aleatorias para cada canal de cores
def cor():
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    r = random.randint(0, 255)
    return b, g, r

#Pega os eventos de mouse
def mouse_click(event, x, y, flags, param): 
    if event == cv2.EVENT_LBUTTONDOWN:
        # a variável C recebe as cores geradas aleatoriamente pela função cor.
        c = cor()
        #Desenhas os pontos com as cores aleatorias geradas na função na posição do click do mouse
        cv2.circle(img, (x, y), 3, c,-1)
        #Mostra a imagem novamente
        cv2.imshow('image', img) 
#Chama a função que pega o evento do mouse
cv2.setMouseCallback('image', mouse_click) 
   
cv2.waitKey(0) 
cv2.destroyAllWindows() 