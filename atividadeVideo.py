import cv2
import random
# capture = cv2.VideoCapture(0)
#Acessa um video
capture = cv2.VideoCapture("videos/IFMA Campus Caxias.mp4")

#Pega a largura e altura da janela
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
#Mostra a largura e altura da janela
print("WIDTH: '{}'".format(frame_width))
print("HEIGHT : '{}'".format(frame_height))

#Define as cores 
b = (255, 0, 0)
g = (0, 255, 0)
r = (0, 0, 255)

#Passa cada cor para uma lista
lista_cor = [b, g, r]

#Lista para armazenar as posições do click do mouse
lista_pos = []
#Define uma cor inicial da lista para a variável c
c = lista_cor[0]

#Função que pega os eventos do mouse
def posicao(event, x, y, flags, param, ):
    #Verifica se foi pressionado o botão esquerdo do mouse
    if event == cv2.EVENT_LBUTTONDOWN:
        #Adiciona a posição do click e a cor na lista 
        lista_pos.append((x, y, c))
#Função que faz a troca aleatória das cores
def troca():
    global c
    pos = random.randint(0, len(lista_cor)-1)
    c = lista_cor[pos]

#Função que desenha o ponto n posição do click
def desenhar():
    for (x, y, c) in lista_pos:
        cv2.circle(frame,(x, y), 3, c, -1)
#Define um nome para a janela
cv2.namedWindow('Video IFMA')
#Passa para a função de evnto do mouse a janela e a posição do click
cv2.setMouseCallback('Video IFMA', posicao)

#Verifica se está sendo acessada a câmera ou um video
if not capture.isOpened():
    print("Erro ao acessar camera")
else:
    #Define o codec para salvar o video
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("video.avi", fourcc, int(fps), (int(frame_width), int(frame_height)), True)
    #Reproduz o video
    while capture.isOpened():
        ret, frame = capture.read()
        if ret is True:
            #Chama a função desenhar
            desenhar()
            #Salva o video
            output.write(frame)
            #Exibe o video na tela
            cv2.imshow('Video IFMA', frame)
            key = cv2.waitKey(20)

            #Fecha o video quando for pressionada a tecla q
            if key & 0xFF == ord('q'):
                break
            #Troca a cor dos pontos quando for pressioada a tecla c
            if key & 0xFF == ord('c'):
                troca()

            #Limpa os desenhos do video quando for pressionada a tecla espaço
            if key & 0xFF == ord(' '):
                lista_pos.clear()

        else: break
output.release()
capture.release()
cv2.destroyAllWindows()