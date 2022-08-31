from microbit import *
import random
import music

led = 0

def led_on(led):
   x = led % 5
   y = led // 5
   display.set_pixel(x, y, 9)

def led_off(led):
   x = led % 5
   y = led // 5
   display.set_pixel(x, y, 0)

answer = None
newgame = True

while True:
   if newgame:
       music.play(music.DADADADUM)
       answer = random.randint(0, 24)
       led_on(answer)
       sleep(2000)
       led_off(answer)
       led_on(led)
       newgame = False

   if pin_logo.is_touched():
       if led == answer:
           music.play(music.BA_DING)
           led_off(led)
           led = 0
           newgame = True
           sleep(1000)
           
   if button_a.was_pressed():
       led_off(led)
       led = led - 1
       if led < 0:
          led = led + 25
       led_on(led)
   if button_b.was_pressed():
       led_off(led)
       led = led + 1
       if led > 24:
          led = led - 25
       led_on(led)
   