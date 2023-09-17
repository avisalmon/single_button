# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on github/avisalmon/TBD
#
# Lesson 1: Basic drawing more
# ****************************************

from machine import Pin, I2C
import ssd1306

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object

# Lets see what else we can draw
display.fill(0)
display.line(0, 0, 63, 63, 1)

# set pixel at x=3, y=10 to colour=1
display.pixel(3, 10, 1)

# draw horizontal line x=0, y=8, width=40, colour=1
display.hline(0, 8, 40, 1)

# draw vertical line x=0, y=8, height=10, colour=1
display.vline(0, 8, 10, 1)

display.rect(10, 10, 30, 30, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
#display.fill_rect(10, 10, 107, 43, 1)   # draw a solid rectangle 10,10 to 117,53, colour=1
display.text('Hello World', 0, 0, 1)    # draw some text at x=0, y=0, colour=1
#display.scroll(20, 0)                   # scroll 20 pixels to the right
display.show()

# more: https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
    

        

# our screen:
# 0,0			127,0
#
# 0,63			127,63


#Now you:
# 1. draw a bold square with diagonals

    

