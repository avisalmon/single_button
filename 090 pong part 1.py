# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on github/avisalmon/TBD
#
# Lesson 1: Pong 1: the stick
# ****************************************

from machine import Pin, I2C
import ssd1306
from font import Font
from time import sleep, ticks_ms

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

button = Pin(4, Pin.IN, Pin.PULL_UP)

stick_pos_x = 50

last_button_status = 0
direction = 1 # 1 is right, -1 is left

while True:
    # clear the screen
    display.fill(0)
    
    #draw the stick
    display.fill_rect(stick_pos_x, 50, 30, 5 , 1)
    display.show()
    
    button_pressed = not button.value()
    
    # calculate new position:
    if button_pressed: # button is pressed
        if last_button_status == 0:
            direction *= -1
        last_button_status = 1
        
        stick_pos_x += 5 * direction
        
    else:
        last_button_status = 0
        
      