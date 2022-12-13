from ctypes import windll, Structure, c_long, byref
import serial, cv2, time, math
ser = serial.Serial('COM8', 9600)  # open serial port
print(ser.name)         # check which port was really used

#stuff to get the mouses location
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def MouseX():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return {pt.x}
	
def MouseY():
	pt=POINT()
	windll.user32.GetCursorPos(byref(pt))
	return {pt.y}

while True:
	#constatnly print the mouses position
	posx = str(MouseX())
	posy = str(MouseY())
	print("X:" + posx + ", Y:" + posy)
	
	
	posx = posx.replace("{", "")
	posy = posy.replace("{", "")
	posx = posx.replace("}", "")
	posy = posy.replace("}", "")
	
	posxInt = int(posx)
	posyInt = int(posy)
	
	x = math.floor(180 - (posxInt / (1600 / 180)))
	y = math.floor(posyInt / (900 / 180))
	
	print(str(x) + ", " + str(y))
	
	ser.write(("X" + str(x) + "Y" + str(y)).encode())
	
	#delay loop
	time.sleep(.05)
	