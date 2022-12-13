import cv2, time

#Create Object. Zero for external camera
video = cv2.VideoCapture(0)
a = 0
while True:
	
	a = a + 1

	#Create a frame object
	check, frame = video.read()

	print(check)
	print(frame) #Representing image

	#Convert to greyscale
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	#Show the frame!
	cv2.imshow("Capturing", gray)

	#For press any key to out (miliseconds)
	#cv2.waitKey(0)

	#For playing
	key=cv2.waitKey(1)
	
	if key == ord('q'):
		break
		
print(a)

#Shutdown camera
video.release()

cv2.destroyAllWindows