# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on github/avisalmon/TBD
#
# Lesson 2: Basic drawing on screen, Moving the lines
# ****************************************

from machine import Pin, I2C
import ssd1306
from time import ticks_ms

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object

# We are using 2 color screen. 0 is black. 1 is white
# clear the screen:
x = 0
y = 0
x_speed = 1
y_speed = 1

while True:
    # prepare the screen
    display.fill(0)
    display.line(x, y, 63, 63, 1)

    # Send the buffer to the screen
    display.show()

    # manipulate the game
    x += x_speed
    if x > 127 or x < 0:
        x_speed *= -1
        

# our screen:
# 0,0			127,0
#
# 0,63			127,63


#Now you:
# 1. Make it faster
# 2. Flip the direction. The top side is still and the bottom is moving. 
# 3. Do something creative with the line. 



