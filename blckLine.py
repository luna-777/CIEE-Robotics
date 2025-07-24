from infrared import Infrared
from motor import Ordinary_Car
import time


infrared = Infrared()
drive = Ordinary_Car()
j = True

while True:
	left = infrared.read_one_infrared(1)
	center = infrared.read_one_infrared(2)
	right = infrared.read_one_infrared(3)
#go forward if all sense white
	if left ==1 and center ==1 and right ==1:
		drive.set_motor_model(650,650,650,650)
		time.sleep(0.5)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
	elif left==0 and center ==1 and right==1:
		drive.set_motor_model(700,700,500,500)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
	elif left==1 and center == 1 and right ==0:
		drive.set_motor_model(500,500,700,700)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
	elif left==1 and center==0 and right ==0:
		drive.set_motor_model(400,400,800,800)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
	elif left==0 and center==0 and right ==1:
		drive.set_motor_model(800,800,400,400)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
	elif left==1 and center==0 and right ==1:
		drive.set_motor_model(650,650,650,650)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
	elif left==0 and center==1 and right ==0:
		drive.set_motor_model(650,650,650,650)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
	elif left==0 and center ==0 and right ==0:
		drive.set_motor_model(-1000,-1000,1000,1000)
		time.sleep(0.2)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
