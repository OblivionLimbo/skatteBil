from microbit import *
import random

svar = ["ja", "nei", "ikke sikker"]

if ( accelerometer.was_gesture("shake") ):
	display.scroll(random.choice(svar))
