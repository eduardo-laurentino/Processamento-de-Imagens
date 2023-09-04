import cv2
import numpy as np

img = cv2.imread('imagens/coins.jpeg')

img_blur = cv2.medianBlur(img, 5)
img_blur = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT,
                           1, 100, param1=150, param2=50)


circles=np.uint(circles[0])
print(circles)

color = (255, 0, 0)
coins = {73:'50', 64:'5', 85:'1', 59:'10', 72:'25'}

for i in circles:
    x, y, r = i
    #print(x,y)
    cv2.circle(img, (x, y), r, color, 3)
    #cv2.circle(img, (x, y), 1, color, 3)

    text = coins[r]
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                1, color, 2, cv2.LINE_AA)

cv2.imshow('Tarefa 2', img)

cv2.waitKey(0)
cv2.destroyAllWindows()