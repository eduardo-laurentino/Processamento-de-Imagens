import cv2
import numpy

brilho=0
contraste=1
negativo=False
imagem = cv2.imread('imagens/logo-if.jpg')

def ajuste_brilho(img, br):
    b, g, r = cv2.split(img)
    b = cv2.add(b, br)
    g = cv2.add(g, br)
    r = cv2.add(r, br)
    res = cv2.merge((b, g, r))
    return res


def ajuste_contraste(img, contraste):
    b, g, r = cv2.split(img)

    b = cv2.divide(b, 255)
    g = cv2.divide(g, 255)
    r = cv2.divide(r, 255)

    b = cv2.multiply(b, contraste)
    g = cv2.multiply(g, contraste)
    r = cv2.multiply(r, contraste)


    result = cv2.merge((b, g, r))
    return result

def ajuste_negativo(img):
    b, g, r = cv2.split(img)
    b = cv2.subtract(255, b)
    g = cv2.subtract(255, g)
    r = cv2.subtract(255, r)
    res = cv2.merge((b, g, r))
    return res


while(True): 
    cv2.imshow('Brilho-Contraste-Negativo', imagem)
    k=cv2.waitKey(20)
    if k == 27:
        break
    elif k == ord('a'):
        brilho += 10
        cv2.imshow('Brilho', ajuste_brilho(imagem, brilho))
    elif k == ord('z'):
        brilho -= 10
        cv2.imshow('Brilho', ajuste_brilho(imagem, brilho))
    elif k == ord('s'):
        contraste += 10
        cv2.imshow('Contraste', ajuste_contraste(imagem, contraste))
    elif k == ord('x'):
        contraste -= 10
        cv2.imshow('Contraste', ajuste_contraste(imagem, contraste))
    elif k == ord('n'):
        cv2.imshow('Negativo', ajuste_negativo(imagem))

cv2.destroyAllWindows()