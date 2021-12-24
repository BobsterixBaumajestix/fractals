import numpy as np
import cv2

arr = np.load('mandelbrot_conv_map.npy')
shape = (arr.shape[0], arr.shape[1], 3)
img = np.zeros(shape, dtype='uint8')

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i][j] == -1:
            img[i][j] = (0, 0, 0)
        elif 1 <= arr[i][j] <= 3:
            img[i][j] = (255, 0, 0)
        elif 4 <= arr[i][j] <= 6:
            img[i][j] = (0, 255, 0)
        elif 7 <= arr[i][j] <= 10:
            img[i][j] = (0, 0, 255)
        else:
            img[i][j] = (255, 255, 255)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
