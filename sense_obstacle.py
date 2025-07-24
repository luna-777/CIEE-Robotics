import time
from ultrasonic import Ultrasonic

dist_sensor = Ultrasonic()

g = True

while g:
    dist = dist_sensor.get_distance()
    print(f"Current distance is {dist} cm")

    time.sleep(1)
    
    if dist <= 10:
        print("There is an obstacle")
        g = False

