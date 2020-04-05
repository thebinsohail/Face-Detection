import cv2

cap=cv2.VideoCapture(0);
while(True):
        ret,frame=cap.read()

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        cv2.imshow('frame',frame)

        if cv2.waitKey(0) & 0xFF==ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()