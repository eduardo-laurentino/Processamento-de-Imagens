import cv2
import random

capture = cv2.VideoCapture("videos/IFMA Campus Caxias.mp4")
img2 = cv2.imread('imagens/logo-if.jpg')

while True:
    ret, frame = capture.read()

    if ret is True:
        img2 = cv2.resize(img2,(200,100),interpolation=cv2.INTER_AREA)

        #Logo no topo esquerdo
        rows,cols,channels = img2.shape

        #Trecho da imagem onde o logo ficará
        roi = frame[0:rows, 0:cols]

        #Cria máscara a partir de escala de cinza
        img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        ret, mask_inv = cv2.threshold(img2gray, 125, 255, cv2.THRESH_BINARY)
        mask = cv2.bitwise_not(mask_inv)

        #Remove máscara da região de interesse
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

        #Filtra somente a máscara obtida pelo threshold
        img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

        dst = cv2.add(img1_bg,img2_fg)

        frame[0:rows, 0:cols ] = dst
        cv2.imshow('Cinza', frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else: 
        break
capture.release()
cv2.destroyAllWindows()