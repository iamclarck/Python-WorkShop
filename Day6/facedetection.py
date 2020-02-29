import cv2
# eye_cascade = cv2.CascadeClassifier(r'C:\Users\Deepak\Desktop\Day6\xml\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    r'C:\Users\Deepak\Desktop\Day6\xml\haarcascade_eye.xml')
image = cv2.imread(r'C:\Users\Deepak\Desktop\Day6\photo.jpg', 1)

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# faces = eye_cascade.detectMultiScale(grey_image,scaleFactor=1.05,minNeighbors=6)
eyes = eye_cascade.detectMultiScale(grey_image,scaleFactor=1.05,minNeighbors=6)
print(eyes)
for x,y,w,h in eyes:
    image = cv2.rectangle(image,(x,y),(x+w,y+w),(25,255,65),3)


cv2.imshow('Grey image Window',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
