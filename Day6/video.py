import cv2

video = cv2.VideoCapture(r'C:\Users\Deepak\Desktop\Day6\faceDetection.mp4')
face_cascade = cv2.CascadeClassifier(r'C:\Users\Deepak\Desktop\Day6\xml\haarcascade_frontalface_default.xml')

while True:
    check,frame = video.read() 

    faces = face_cascade.detectMultiScale(frame,scaleFactor=1.05,minNeighbors=5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),3)


    cv2.imshow('Grey image Window',frame)
    key = cv2.waitKey(5)
    if (key==ord('q')):
        break

cv2.destroyAllWindows()
video.release()
