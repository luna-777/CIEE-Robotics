from infrared import Infrared
from motor import Ordinary_Car
import time
from buzzer import Buzzer
from adc import ADC

buzzer2=Buzzer()
adc = ADC()

infrared = Infrared()
drive = Ordinary_Car()
j = True
d=""
LINE_ON = 0
LINE_OFF = 1
#reads the line
def readLine():
	left = infrared.read_one_infrared(1)
	center = infrared.read_one_infrared(2)
	right = infrared.read_one_infrared(3)
	return (left, center, right)

#beep function that stops the car when it reaches the end
def end():
	drive.set_motor_model(0,0,0,0)
	for _ in range(3):
		buzzer2.set_state(True)
		time.sleep(0.1)
		buzzer2.set_state(False)
		time.sleep(0.1)
	adc.close_i2c()
	stop()

def stop():
	drive.set_motor_model(0,0,0,0)
left_idr = adc.read_adc(0)
right_idr = adc.read_adc(1)
#if goes off line, this function puts it back on
def lineFind():
	count = 0
	speed = 600
	left = infrared.read_one_infrared(1)
	center = infrared.read_one_infrared(2)
	right = infrared.read_one_infrared(3)
	while left==LINE_OFF and center ==LINE_OFF and right ==LINE_OFF:
		left = infrared.read_one_infrared(1)
		center = infrared.read_one_infrared(2)
		right = infrared.read_one_infrared(3)

		if left == LINE_ON or center == LINE_ON or right == LINE_ON:
			print("found line1")
			break

		if count <= 10:
			# turn slightly left
			print("micro turn: left")
			drive.set_motor_model(-speed,-speed,speed,speed)
		elif count <= 35:
			# turn slightly right
			print("micro turn: right")
			drive.set_motor_model(speed,speed,-speed,-speed)
		else:
			count = 0
			continue

		time.sleep(0.13)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.5)
		count += 1
while True:
	left, center, right = readLine()

	if left ==LINE_ON and center ==LINE_ON and right ==LINE_ON:
		print("forward")
		drive.set_motor_model(650,650,650,650)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.2)
	elif left==LINE_OFF and center ==LINE_ON and right==LINE_ON:
		print("left")
		drive.set_motor_model(700,700,0,0)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.2)
	elif left==LINE_ON and center == LINE_ON and right ==LINE_OFF:
		print("right")
		drive.set_motor_model(0,0,700,700)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.2)
	elif left==LINE_ON and center==LINE_OFF and right ==LINE_OFF:
		print("hard right")
		drive.set_motor_model(0,0,800,800)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.2)
	elif left==LINE_OFF and center==LINE_OFF and right ==LINE_ON:
		print("hard left")
		drive.set_motor_model(800,800,0,0)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.2)
	elif left==LINE_ON and center==LINE_OFF and right ==LINE_ON:
		print("forward")
		drive.set_motor_model(650,650,650,650)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.2)
	elif left==LINE_OFF and center==LINE_ON and right ==LINE_OFF:
		print("forward")
		drive.set_motor_model(650,650,650,650)
		time.sleep(0.1)
		drive.set_motor_model(0,0,0,0)
		time.sleep(0.2)
	elif left==LINE_OFF and center ==LINE_OFF and right ==LINE_OFF:
		lineFind()

	left_idr = adc.read_adc(0)
	right_idr = adc.read_adc(1)
#checks for the light at the end of the maze, and calls end method for beeps and stop
	if float(left_idr)>=4.5 or float(right_idr)>=4.5:
		end()

try:
        pass
except KeyboardInterrupt:
        stop()
