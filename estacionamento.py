import cv2
import numpy as np

#Mapeamento das vagas
vaga1 = [1, 89, 108, 213]
vaga2 = [115, 87, 152, 211]
vaga3 = [289, 89, 138, 212]
vaga4 = [439, 87, 135, 212]
vaga5 = [591, 90, 132, 206]
vaga6 = [738, 93, 139, 204]
vaga7 = [881, 93, 138, 201]
vaga8 = [1027, 94, 147, 202]

vagas = [vaga1, vaga2, vaga3, vaga4, vaga5, vaga6, vaga7, vaga8]

video = cv2.VideoCapture("videos/video.mp4")
while True:
    checked, imagem = video.read()
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_trashold = cv2.adaptiveThreshold(imagem_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imagem_blour = cv2.medianBlur(imagem_trashold, 5)
    kernel = np.ones((3, 3), np.int8)
    imagem_dilatada = cv2.dilate(imagem_blour, kernel)

    for x, y, largura, altura in vagas:
        recorte = imagem_dilatada[y:y + largura, x:x + altura]
        qtdpxbranco = cv2.countNonZero(recorte)
        cv2.putText(imagem, str(qtdpxbranco), (x, y + altura - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 255, 0), 3)
        if(qtdpxbranco > 4000):
            cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 0, 255), 3)
        else:
            cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 255, 0), 3)
    cv2.imshow('Video Original', imagem)
    #cv2.imshow('Video', imagem_trashold)
    cv2.waitKey(10)
    
cv2.destroyAllWindows()