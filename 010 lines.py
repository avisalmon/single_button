# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on https://github.com/avisalmon/single_button
#
# Lesson 1: Basic drawing on screen, Lines
#
# Make sure to download to the device all files in directory "Upload_this_to_device"
# ****************************************


# Setting imports, and display

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


#Now you:
# 1. Draw a big X on the screen
# 2. Draw your name Third letter.
 

