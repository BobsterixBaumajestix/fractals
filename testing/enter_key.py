import cv2

img = cv2.imread('../colortest.png')
cv2.imshow('test', img)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
print(key)
