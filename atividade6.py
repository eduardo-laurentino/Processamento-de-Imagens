import cv2 

img = cv2.imread('imagens/image.jpg')
cv2.imshow('image', img)
(alt, lar) = img.shape[:2]
def mouse_click(event, x, y, flags, param): 
    if event == cv2.EVENT_LBUTTONDOWN:
        ponto = (x, y) #ponto no centro da figura
        rotacao = cv2.getRotationMatrix2D(ponto, 45, 1.0)
        rotacionado = cv2.warpAffine(img, rotacao, (alt, lar))
        cv2.imshow('image', rotacionado) 


cv2.setMouseCallback('image', mouse_click) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
