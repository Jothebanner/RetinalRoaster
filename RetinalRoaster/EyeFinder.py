import numpy as np
import cv2 as cv
import time
import serial
ser = serial.Serial('COM8', 9600)  # open serial port
print(ser.name)         # check which port was really used
face_cascade = cv.CascadeClassifier('C:\\Users\\Slugger\\Desktop\\ProjectsCodehaarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:\\Users\\Slugger\\Desktop\\ProjectsCodehaarcascade_righteye_2splits.xml')
video = cv.VideoCapture(0)

a = 0
while True:
	
	a = a + 1
	
	check, frame = video.read()

	#Convert to greyscale
	gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
			print ("X:" + str(ex) + ", Y:" + str(ey))
			ser.write(("X" + str(x) + "Y" + str(y)).encode())
	cv.imshow('Target',frame)
	#For playing
	key=cv.waitKey(1)
	
	if key == ord('q'):
		break
		
print(a)

#Shutdown camera
video.release()

cv.destroyAllWindows

#debug
input()