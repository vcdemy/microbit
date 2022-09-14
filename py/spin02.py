from microbit import *
import random
import music

x0 = 2
y0 = 0

spin = False
x = 0
y = 0

xstep = 0
ystep = 0

success = 0
fail = 0

while True:
    
    display.set_pixel(x, y, 9)
    display.set_pixel(x0, y0, 9)
    if pin_logo.is_touched():
        display.scroll("{}:{}".format(success, fail))
    
    if button_a.was_pressed():
        spin = True
    if button_b.was_pressed():
        if x == x0 and y == y0:
            music.play(music.JUMP_UP)
            success += 1
        else:
            music.play(music.JUMP_DOWN)
            fail += 1
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

        # music.pitch(500, 10)
        sleep(50)
        
        display.set_pixel(x, y, 0)
        display.set_pixel(x0, y0, 9)
        x = x + xstep
        y = y + ystep

    
    