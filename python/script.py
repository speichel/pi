import webiopi
import datetime

GPIO = webiopi.GPIO

LIGHT = 17 # GPIO pin using BCM numbering
SERVO_1A = 21 #GPIO pin, to arduino for SERVO_1A control 
SERVO_1B = 22 #GPIO pin, to arduino for SERVO_1B control 
SERVO_2A = 23 #GPIO pin, to arduino for SERVO_2A control 
SERVO_2B = 24 #GPIO pin, to arduino for SERVO_2B control 

HOUR_ON  = 8  # Turn Light ON at 08:00
HOUR_OFF = 18 # Turn Light OFF at 18:00

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.OUT)
    GPIO.setFunction(SERVO_1A, GPIO.OUT)
    GPIO.setFunction(SERVO_1B, GPIO.OUT)
    GPIO.setFunction(SERVO_2A, GPIO.OUT)
    GPIO.setFunction(SERVO_2B, GPIO.OUT)

    # retrieve current datetime
    now = datetime.datetime.now()

    # test if we are between ON time and turn the light ON
    if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)): 
        if (GPIO.digitalRead(LIGHT) == GPIO.LOW): 
       	    PIO.digitalWrite(LIGHT, GPIO.HIGH)

# toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)): 
        if (GPIO.digitalRead(LIGHT) == GPIO.HIGH): 
            GPIO.digitalWrite(LIGHT, GPIO.LOW)
	
    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)
    GPIO.digitalWrite(SERVO_1A, GPIO.LOW)
    GPIO.digitalWrite(SERVO_1B, GPIO.LOW)
    GPIO.digitalWrite(SERVO_2A, GPIO.LOW)
    GPIO.digitalWrite(SERVO_2B, GPIO.LOW)
