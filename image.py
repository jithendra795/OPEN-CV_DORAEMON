import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('d.jpg')
blue = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(blue, 1.1, 4)
for (d, n, s, j) in faces:
    cv2.rectangle(img, (d, n), (d + n, s + j), (255, 0, 0), 2)
cv2.imshow('img', img)
cv2.waitKey() 
