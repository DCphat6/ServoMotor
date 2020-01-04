import RPi.GPIO as GPIO
import time

#servoPIN = 17
#GPIO.setmode(GPIO.BCM)

servoPIN = 11
GPIO.setmode(GPIO.BOARD)

GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 11 for PWM with 50Hz
p.start(2.5) # Initialization
#p.ChangeDutyCycle(5)
#time.sleep(0.5)
print("Center")
p.ChangeDutyCycle(7.5)
time.sleep(2)
print("Right")
p.ChangeDutyCycle(3.5)
time.sleep(3)
print("left")
p.ChangeDutyCycle(12.5)
time.sleep(2)
print("Center")
p.ChangeDutyCycle(7.5)
time.sleep(2)
p.stop()
print("Done")
GPIO.cleanup()
