# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on github/avisalmon/TBD
#
# Lesson 1: Text
# ****************************************

# Make sure to upload all files in the directory Upload_these_to_device to the dvice.
# Right click on the files and upload. 

from machine import Pin, I2C
import ssd1306
from font import Font

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object

display.fill(0)

# simple built in text:
display.text('First Line', 0, 0, 1)
display.text('Second Line', 0, 10, 1)
display.text('placed Line', 40, 20, 1)

# special fonts:
f=Font(display)
#f.text("8",0,50,8) #8 pix
f.text("16",0,30,16) #16 pix
f.text("24",30,30,24) #24 pix
f.text("32",60,30,32) #32 pix

display.show()

# our screen:
# 0,0			127,0
#
# 0,63			127,63


#Now you:
# 1. Write your name. Big time. and your fhone smaller. 

    


