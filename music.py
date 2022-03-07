from microbit import *
import music
# Imports Music
# music.set_tempo(ticks=4,bpm=149)
# Set Tempo

#Tetris Theme
notes = [
'e','b', 'c','d', 'c','b', 'a',
'a', 'c','e','d', 'c','b',
'c','d', 'e','c','a', 'a',
'd', 'f', 'a', 'g', 'f', 'e',
'c','e','d', 'c','b',
'b', 'c','d', 'e','c','a', 'a',
'e','b', 'c','d', 'c','b', 'a',
'a', 'c','e','d', 'c','b',
'c','d', 'e','c','a', 'a',
'd', 'f', 'a', 'g', 'f', 'e',
'c','e','d', 'c','b',
'b', 'c','d', 'e','c','a', 'a',
'e','c','d', 'b', 'c','a', 'a','b', 'b',
'e','c','d', 'b', 'c','e','a', 'a','b',
'e','b', 'c','d', 'c','b', 'a',
'a', 'c','e','d', 'c','b',
'c','d', 'e','c','a', 'a',
'd', 'f', 'a', 'g', 'f', 'e',
'c','e','d', 'c','b',
'b', 'c','d', 'e','c','a', 'a',
'e','b', 'c','d', 'c','b', 'a',
'a', 'c','e','d', 'c','b',
'c','d', 'e','c','a', 'a',
'd', 'f', 'a', 'g', 'f', 'e',
'c','e','d', 'c','b',
'b', 'c','d', 'e','c','a', 'a',
'e','c','d', 'b', 'c','a', 'a','b', 'b',
'e','c','d', 'b', 'c','e','a', 'a','b',
'e','b', 'c','d', 'c','b', 'a',
'a', 'c','e','d', 'c','b',
'c','d', 'e','c','a', 'a',
'd', 'f', 'a', 'g', 'f', 'e',
'c','e','d', 'c','b',
'b', 'c','d', 'e','c','a', 'a'
] 

music.play(notes)