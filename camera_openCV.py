import cv2
#Fatiamento e desenho sobre a imagem
#Acessa a câmera
cap = cv2.VideoCapture(0)
n = 0

#Faz a leitura de cada frame da câmera
while(True):
    ok, frame = cap.read()
    if not ok :
        break
    #conta a quantidade de frames
    n = n+1
    #Escreve a quantidade de frames
    cv2.putText(frame, str(n), (100, 200), cv2.FONT_ITALIC, 1, (0, 0, 255), cv2.LINE_4)
    #Exibe os frames na janela
    cv2.imshow('frame', frame)
    #Fecha a janela quando pressionar a tecla q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

