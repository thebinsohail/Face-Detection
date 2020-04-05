import cv2
img=cv2.imread('anas.jpg',0)
cv2.imshow('my picture',img)

k=cv2.waitKey(0)

if k==27:
        cv2.destroyAllWindows()

