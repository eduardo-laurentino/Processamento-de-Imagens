import cv2
img = cv2.imread('imagens/foto.jpeg')
img = cv2.resize(img,(150, 250))
cv2.imshow('Resize', img)
cv2.imwrite('img_resize.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows