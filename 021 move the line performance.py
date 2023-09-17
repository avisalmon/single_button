# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on github/avisalmon/TBD
#
# Lesson 1: Basic drawing on screen, Moving the lines
# ****************************************

from machine import Pin, I2C
import ssd1306
from time import ticks_ms
import machine

machine.freq(240000000)

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object

# We are using 2 color screen. 0 is black. 1 is white
# clear the screen:
x = 0
y = 0
x_speed = 1
y_speed = 1

t1 = 0

while True:
    display.fill(0)
    display.line(x, y, 63, 63, 1)
    t_prep = ticks_ms() - t1
    ts = ticks_ms()
    display.show()
    t_show = ticks_ms() - ts
    t1 = ticks_ms()
    x += x_speed
    if x > 127 or x < 0:
        x_speed *= -1
    print(f'prep: {t_prep}ms ; show: {t_show}ms')
        

# our screen:
# 0,0			127,0
#
# 0,63			127,63


#Now you:
# 1. Make it faster
# 2. Make the other end of the line move as well
# 3. Do something creative with the line. 


