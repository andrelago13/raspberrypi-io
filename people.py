#####################################################################
# This program uses a PIR sensor to signal the presence of a person #
# When a person is detected, a message is written and an LED is lit #
#                                                                   #
# WIRING:                                                           #
#  having the lamp facing forward (or looking at the bottom of the  #
#  sensor, with the main 3-pin set on the top:                      #
#    Left: GND                                                      #
#    Center: Signal ('sensor_pin' pin)                              #
#    Right: 5V                                                      #
#    Switch: with the "border" pin free (repeating-trigger mode)    #
# ###################################################################
import RPi.GPIO as GPIO
import time

light_pin = 18
sensor_pin = 7
time_limit = 2000
period = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(light_pin, GPIO.OUT)

previous = 0
people_count = 0
i = time_limit
print "start"
while(i > 0):
    i = i - 1
    presence = GPIO.input(sensor_pin)
    GPIO.output(light_pin, presence)
    if(presence == 1 and previous == 0):
        people_count += 1
        print "Person Detected! (" + `people_count` + ")"
    time.sleep(period)
    previous = presence
