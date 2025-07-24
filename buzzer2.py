from buzzer import Buzzer
import time

buzzer2=Buzzer()
try:
	for _ in range(3):
		buzzer2.set_state(True)
		time.sleep(0.1)
		buzzer2.set_state(False)
		time.sleep(0.1)
finally:
	buzzer2.close()
