# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on github/avisalmon/TBD
#
# Lesson 1: Basic drawing on screen, Lines
# ****************************************

from machine import Pin, I2C
import ssd1306

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object

# We are using 2 color screen. 0 is black. 1 is white
# clear the screen:
display.fill(0)
display.line(30, 10, 50, 50, 1)
display.show()

# our screen:
# 0,0			127,0
#
# 0,63			127,63

display.line(0, 0, 127, 0, 1)
display.line(127, 0, 127, 63, 1)
display.line(127, 63, 0, 63, 1)
display.line(0, 63, 0, 0, 1)

display.show()



#Now you:
# 1. Draw your name Third letter.
# 2. Not a must: Draw squares on all the screen like a squared paper.

