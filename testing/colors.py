import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype='uint8')
font = cv2.FONT_HERSHEY_SIMPLEX


for i in range(500):
    for j in range(500):
        img[i][j] = (100.5, 255, 255)

img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


