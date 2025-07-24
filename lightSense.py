import time
from adc import ADC
from buzzer import Buzzer
import time
buzzer2=Buzzer()
adc = ADC()

try:
	while True:
		left_idr = adc.read_adc(0)
		right_idr = adc.read_adc(1)
		print(f"Left IDR: {left_idr}V, Right IDR: {right_idr}V")
		time.sleep(1)
		if float(left_idr)>=4.5 or float(right_idr)>=4.5:
			for _ in range(3):
				buzzer2.set_state(True)
				time.sleep(0.1)
				buzzer2.set_state(False)
				time.sleep(0.1)
			adc.close_i2c()
except KeyboardInterrupt:
	adc.close_i2c()
	buzzer2.close()
