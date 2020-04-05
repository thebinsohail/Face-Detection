import cv2

#define classifier 
face_cascader=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread("Anas.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascader.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)


cv2.imshow('Anas',img)
cv2.waitKey(0)