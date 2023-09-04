import cv2
import random

global x, y

def mouse_click(event, x, y, flags, param): 
    if event == cv2.EVENT_LBUTTONDOWN:
        # a variável C recebe as cores geradas aleatoriamente pela função cor.
        c = cor()
        #Desenhas os pontos.
        cv2.circle(frame, (x, y), 3, c,-1)

def pos():
    x = random.randint(0, 1000)  
    y = random.randint(0, 1000)
    return x, y
def cor():
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    r = random.randint(0, 255)
    return b, g, r

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("videos/IFMA Campus Caxias.mp4")
while True:
    ret, frame = capture.read()
    if ret is True:
        aux = pos()
        c = cor()
        #Video original
        #cv2.imshow('Input', frame)

        #Video em escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.circle(frame, aux , 10, c,-1)
        #cv2.circle(frame, (500, 500) , 10, c,-1)
        cv2.imshow('Cinza', frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        if cv2.waitKey(20) & 0xFF == ord('w'):
            #Tira print do video normal em escala de cinza
            print("Salvando frame...")
            cv2.imwrite('print.jpg',frame)
            cv2.imwrite('gray.jpg',gray)
    else: 
        break
capture.release()
cv2.destroyAllWindows()
