
from motor import Ordinary_Car
import time

drive=Ordinary_Car()
drive.set_motor_model(1000, 1000, 1000, 1000)
print ("The car is moving forward")
time.sleep(1)
drive.set_motor_model(-1000, -1000, -1000, -1000) 
print ("The car is going backwards")
time.sleep(1)
drive.set_motor_model(-1500, -1500, 2000, 2000)
print ("The car is turning left")
time.sleep(1)
drive.set_motor_model(2000, 2000, -1500,-1500)
print ("The car is turning right")
time.sleep(1)
drive.set_motor_model(0,0,0,0)
print ("\nEnd of program")


def drive_forward():
	drive.set_motor_model(1000, 1000, 1000, 1000)
	print ("The car is turning right")
	time.sleep(1)
def drive_backward():
	drive.set_motor_model(-1000,-1000, -1000, -1000)
	print ("The car is turning right")
	time.sleep(1)
def drive_left():
	drive.set_motor_model(-1500,-1500,2000,2000)
	print ("The car is turning left")
	time.sleep(1)
def drive_right():
	print ("The car is turning right")
	time.sleep(1)
	drive.set_motor_model(2000,2000,-1500,-1500)
def stop():
	drive.set_motor_model(0,0,0,0)
	print ("\nEnd of program")
def slide_left():
	print ("The car is sliding left")
	drive.set_motor_model(-1000,1000,1000,-1000)
	time.sleep(1)
def slide_right():
        print ("The car is sliding right")
        drive.set_motor_model(1000,-1000,-1000,1000)
        time.sleep(1)
def right_diag_up():
	print ("The car is going right diagonally up")
	drive.set_motor_model(1000,0,0,1000)
	time.sleep(1)
def left_diag_up():
	print ("The car is going left diagonally up")
	drive.set_motor_model(0,1000,1000,0)
	time.sleep(1)
def right_diag_down():
	print("The car is going right diagonally down")
	drive.set_motor_model(0,-1000,-1000,0)
	time.sleep(1)
def left_diag_down():
	print("The car is going left diagonally down")
	drive.set_motor_model(-1000,0,0,-1000)
	time.sleep(1)
slide_left()
slide_right()
right_diag_up()
right_diag_down()
left_diag_up()
left_diag_down()
stop()
