from microbit import *

# SOS in LEDs
while True:
    for x in range (0,3,1):
        pin2.write_digital(1)
        sleep(250)
        pin2.write_digital(0)
        sleep(250)
    for x in range (0,3,1):
        pin2.write_digital(1)
        sleep(500)
        pin2.write_digital(0)
        sleep(500)
    for x in range (0,3,1):
        pin2.write_digital(1)
        sleep(250)
        pin2.write_digital(0)
        sleep(250)
