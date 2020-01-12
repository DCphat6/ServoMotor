import RPi.GPIO as GPIO
import time
import os


def SetAngle(angle):
	duty = (int(angle) / 18) + 3.5
	print(duty)
	return duty

	
# Give the user some context.
print("\nYou can adjust your servo here. What would you like to do?")

# Set an initial value for choice other than the value for 'quit'.
choice = ''
servoPIN = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 11 for PWM with 50Hz
p.start(0) # Initialization

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[l] Enter l to move servo to the left")
    print("[r] Enter r to move servo to the right.")
    print("[m] Enter m to move servo to the middle.")
    print("[a] Enter your own angle.")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")
    
    # Respond to the user's choice.
    if choice == 'l':
        print("\nMoving to the Left\n")
        p.ChangeDutyCycle(12.5)
        #time.sleep(1)
    elif choice == 'r':
        print("\nMoving to the Right\n")
        p.ChangeDutyCycle(3.5)
        #time.sleep(1)
    elif choice == 'm':
        print("\nMove to the middle\n")
        p.ChangeDutyCycle(7.5)
        #time.sleep(1)
    elif choice == 'a':
        print("\nSoon pick angle\n")
        choice2 = input("\What angle would you like? ")
        MyNumber = SetAngle(choice2)
        print ("back")
        print (MyNumber)
        p.ChangeDutyCycle(MyNumber)
        #time.sleep(1)
    elif choice == 'q':
        print("\nThanks for using my servo adjuster.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
        
# Print a message that we are all finished.
print("Thanks again, bye now.")
p.stop()
GPIO.cleanup()
