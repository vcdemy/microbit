from microbit import *
import random
import music

led = 0
c = 3

def led_on(led):
   x = led % 5
   y = led // 5
   display.set_pixel(x, y, 9)

def led_off(led):
   x = led % 5
   y = led // 5
   display.set_pixel(x, y, 0)

def show_answer(answer):
    for x in answer:
        led_on(x)

answer = []
newgame = True

while True:
   if newgame:
       music.play(music.JUMP_UP)
       answer = []
       n = 0
       while n < c:
           x = random.randint(0, 24)
           if x in answer:
               continue
           answer.append(x)
           n = n + 1
       show_answer(answer)
       sleep(2000)
       display.clear()
       led_on(led)
       newgame = False

   if pin_logo.is_touched():
       if led in answer:
           music.play(music.BA_DING)
           answer.remove(led)
           if not answer:
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
   