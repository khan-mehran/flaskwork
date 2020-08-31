import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) #for using default camera
# cap.set(3,640)
# cap.set(4,480)

while True:
	success, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

	cv2.imshow('img',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break  
	
cap.release()
cv2.destroyAllWindows()