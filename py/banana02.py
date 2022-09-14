from microbit import *
import random
import music

x = 2
y = 4

def new_row():
  a =['0']*5
  a[random.randint(0, 4)]='9'
  return ''.join(a)

leds = ['00000']*5

display.set_pixel(x, y, 9)

delay = 10000
counter = 0

while True:
    # display image
    if counter > delay:
        display.show(Image(':'.join(leds)))
        leds.insert(0, new_row())
        row = leds.pop()
        display.set_pixel(x, y, 9)
        if row[x] == '9':
            music.play(music.BA_DING)
        else:
            if '9' in row:
                music.play(music.JUMP_DOWN)
        counter = counter - delay
        delay = delay - 1
    
    # # control the movement of the led at the bottom row
    if button_a.was_pressed():
        display.set_pixel(x, y, 0)
        x = x - 1
        if x < 0:
            x = 4
        display.set_pixel(x, y, 9)
    if button_b.was_pressed():
        display.set_pixel(x, y, 0)
        x = x + 1
        if x > 4:
            x = 0
        display.set_pixel(x, y, 9)

    counter = counter + 1