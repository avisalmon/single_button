# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on https://github.com/avisalmon/single_button
#
# Lesson 8: Few Player move. Example how to program in object oriented
# ****************************************

from machine import Pin, I2C
import ssd1306
from font import Font
from time import sleep, ticks_ms

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

class Player():
    def __init__(self, x_pos, y_pos, x_speed, y_speed, size):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.size = size
        
    def move(self):
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
        if self.x_pos > 127 or self.x_pos < 0 :
            self.x_speed *= -1
        if self.y_pos > 63 or self.y_pos < 0:
            self.y_speed *= -1

# Create 4 players
players = []
for n in range(4):
    players.append(Player(n*10, n*10, n, n*2, 10))
    
while True:
    display.fill(0)
    #draw all players
    for n in range(4):
        display.fill_rect(players[n].x_pos, players[n].y_pos, 10, 10 , 1)
        players[n].move()
    display.show()
                   
    