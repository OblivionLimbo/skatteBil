from microbit import *

while True:
    if(pin1.read_analog() > 800):
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)
