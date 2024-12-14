# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on https://github.com/avisalmon/single_button
#
# Lesson 6: Blit
# ****************************************


from machine import Pin, I2C
import ssd1306
from font import Font
from time import sleep, ticks_ms

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

display.fill(0)
display.fill_rect(0, 0, 40, 30, 1)
display.show()

import framebuf
#  https://docs.micropython.org/en/latest/library/framebuf.html

fbuf = framebuf.FrameBuffer(bytearray(16 * 16 * 1), 16, 16, framebuf.MONO_VLSB)
fbuf.line(0, 0, 15, 15, 1)
display.blit(fbuf, 20, 20, 0)           # draw on top at x=10, y=10, key=0 (0 or 1. if -1 it will simply blit it all as is )
display.show()

                            