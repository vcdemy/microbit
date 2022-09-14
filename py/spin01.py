from microbit import *
import random
import music

x0 = 2
y0 = 0

display.set_pixel(x0, y0, 9)

spin = False
x = 0
y = 0

xstep = 0
ystep = 0

while True:
    
    display.set_pixel(x, y, 9)
    
    if button_a.was_pressed():
        spin = True
    if button_b.was_pressed():
        spin = False

    if spin:
        if x==0 and y==0:
            xstep = 1
            ystep = 0
        elif x==4 and y==0:
            xstep = 0
            ystep = 1
        elif x==4 and y==4:
            xstep = -1
            ystep = 0
        elif x==0 and y==4:
            xstep = 0
            ystep = -1
        
        sleep(50)
        
        display.set_pixel(x, y, 0)
        display.set_pixel(x0, y0, 9)
        x = x + xstep
        y = y + ystep

    
    