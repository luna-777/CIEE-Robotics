import time
from ultrasonic import Ultrasonic

dist_sensor = Ultrasonic()

while True:
	dist = dist_sensor.get_distance()
	print(f"Current distance is {dist} cm")

	time.sleep(1)
