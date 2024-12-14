# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on https://github.com/avisalmon/single_button
#
# Lesson 5: Read the button
# ****************************************

# Connect the button to pin D4 and ground.  

from machine import Pin, I2C
import ssd1306
from font import Font
from time import sleep,  ticks_ms

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

button = Pin(4, Pin.IN, Pin.PULL_UP)

display.fill(0)

for n in range(10):
    print(button.value())
    sleep(0.3)

display.fill(0)

if button.value() == 1:
    f.text("1",60,30,32)
else:
    f.text("0",60,30,32)

display.show()
    
sleep(5)

    
while True:
    display.fill(button.value())
    display.show()

# Now you:

# 1. Print your name if the button is clicked, else your family name. 

