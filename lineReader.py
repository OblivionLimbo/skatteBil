from microbit import *

def getLine(bit):
    mask = 1 << bit
    value = 0
    try:
        value = i2c.read(0x1c, 1)[0]
    except OSError:
        pass
    if (value & mask) > 0:
        return 1
    else:
        return 0

while True:
    if (getLine(0) == 0 and getLine(1) == 0): # Begge sensorer er utenfor den sorte linja
        pin16.write_digital(1) # Kjører rett frem
        pin8.write_digital(0)
        pin14.write_digital(1) # Kjører rett frem
        pin12.write_digital(0)
    elif (getLine(0) == 1 and getLine(1) == 0): # Hvis venstre sensor går på den sorte linja vil den svinge til høyre
        pin16.write_digital(0)
        pin8.write_digital(1) # Snur motsatt hjul for å snu raskere
        pin14.write_digital(1) # Kjører til høyre
        pin12.write_digital(0)
    elif (getLine(1) == 1 and getLine(0) == 0): # Hvis høyre sensor går på den sorte linja på vil den svinge til venstre
        pin16.write_digital(1) # Kjører til vensre
        pin8.write_digital(0)
        pin14.write_digital(0)
        pin12.write_digital(1) # Snur motsatt hjul for å snu raskere
    elif : # Stopper å kjøre
        pin16.write_digital(0)
        pin8.write_digital(0)
        pin14.write_digital(0)
        pin12.write_digital(0)

