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

while True:
    # display image
    display.show(Image(':'.join(leds)))
    leds.insert(0, new_row())
    leds.pop()
    sleep(2000)

    # control the movement of the led at the bottom row
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
    