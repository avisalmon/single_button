# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on https://github.com/avisalmon/single_button
#
# Lesson 7: single Player move
# ****************************************

from machine import Pin, I2C
import ssd1306
from font import Font
from time import sleep, ticks_ms

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

player_position_x = 0
player_position_y = 0
player_speed_x = 1
player_speed_y = 2

while True:
    # clear the screen
    display.fill(0)
    
    #draw the player
    display.fill_rect(player_position_x, player_position_y, 10, 10 , 1)
    display.show()
    
    # calculate new position:
    player_position_x += player_speed_x
    player_position_y += player_speed_y
    if player_position_x > 127 or player_position_x < 0 :
        player_speed_x *= -1
    if player_position_y > 63 or player_position_y < 0:
        player_speed_y *= -1
    
# Now you:
# 1. make the player go only horizontaly.
# 2. Make the player be thin and wide. 