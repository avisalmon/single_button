# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on github/avisalmon/TBD
#
# Example 1: watch
# ****************************************

from machine import Pin, I2C, PWM, Timer
import machine
import ssd1306
from font import Font
import time
from time import sleep, ticks_ms
import random
import network
import ntptime
import utime

try:
    from keys import SSID, PASSWORD
except:
    SSID = '****'
    PASSWORD = '****'
    
print(PASSWORD, SSID)

from math import sin, cos, pi

buzzer_pin = Pin(23, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.duty(0)

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

def draw_circle(display, x, y, radius, steps = 2):
    for angle in range(0, 360, steps):  # Draw circle with 5-degree increments
        radian_angle = angle * pi / 180
        circle_x = x + int(radius * cos(radian_angle))
        circle_y = y + int(radius * sin(radian_angle))
        display.pixel(circle_x, circle_y, 1)
    #display.show()  # Update the display after drawing the circle

def draw_clock_num(display, x, y, radius, number):
    if n > 9:
        x -= 5
    angle = 90 - number*30
    radian_angle = angle * pi / 180
    x_pos = int(x + radius * cos(radian_angle))
    y_pos = int(y - radius * sin(radian_angle))
    display.text(str(number), x_pos, y_pos, 1)
    
def draw_mahog(display, hour, min, sec, x, y, radius):
    draw_circle(display, x, y, 4, steps=20)
    
    hour_angle_radian = ((90 - (hour*30 + min*0.1)) * pi / 180)
    hour_point_x = int(x + (radius - 15)*cos(hour_angle_radian))
    hour_point_y = int(y - (radius - 15)*sin(hour_angle_radian))
    display.line(x, y, hour_point_x, hour_point_y, 1)
    display.line(x+1, y+1, hour_point_x+1, hour_point_y+1, 1)
    display.line(x-1, y-1, hour_point_x-1, hour_point_y-1, 1)

    min_angle_radian = (90 - min*6) * pi / 180
    min_point_x = int(x + (radius-10)*cos(min_angle_radian))
    min_point_y = int(y - (radius-10)*sin(min_angle_radian))
    display.line(x, y, min_point_x, min_point_y, 1)
    display.line(x+1, y+1, min_point_x+1, min_point_y+1, 1)
    #display.line(x-1, y-1, hour_point_x-1, hour_point_y-1, 1)
    
    sec_angle_radian = (90 - sec*6) * pi / 180
    sec_point_x = int(x + (radius-10)*cos(sec_angle_radian))
    sec_point_y = int(y - (radius-10)*sin(sec_angle_radian))
    display.line(x, y, sec_point_x, sec_point_y, 1)

# Connect to Wifi and get the time from the Internet
station = network.WLAN(network.STA_IF)
station.active(True)
sleep(1)
# change the SSID and PASSWORD to your WiFi credentials, as text
station.connect(SSID, PASSWORD)

while station.isconnected() == False:
    pass
print('Connected')

ntptime.settime()

while time.localtime()[0] < 2000:  # Waiting until the year is set (an indication that time is set)
    pass

# Adjust the time to UTC+3
utc_time = utime.mktime(utime.localtime())
utc_plus_3 = utc_time + 3 * 3600  # Add 2 hours (2 * 3600 seconds) for UTC+2

# Convert back to local time
local_time = utime.localtime(utc_plus_3)

def convert_time_to_ms(hour, min, sec):
    return (sec*1000 + min*60*1000 + hour*60*60*1000)% 86400000

def convert_ms_to_time(ms_count):
    seconds = ms_count // 1000
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds
    
def convert_machine_ms_to_time(sampled_ms, sampled_time_in_ms):
    now = ticks_ms()
    delta = now - sampled_ms
    new_time_ms = (sampled_time_in_ms + delta) % 86400000
    return convert_ms_to_time(new_time_ms)
    

# Print the adjusted local time (UTC+2)
print("Adjusted Local Time (UTC+3):", local_time)
hour, min, sec = local_time[3], local_time[4], local_time[5]
sampled_time_in_ms = convert_time_to_ms(hour, min, sec)
print(f'Sampled time in ms: {sampled_time_in_ms}')
sampled_ms = ticks_ms()

print(f'Sampled machine ms:{sampled_ms}')



while True:
    # number of ms a day is 86400000 ms
    # every hour is 3600000 ms
    # every minute is 60000 ms
    # every second is 1000 ms

    hour, min, sec = convert_machine_ms_to_time(sampled_ms, sampled_time_in_ms)
    
    display.fill(0)  # Clear the display
    draw_circle(display, 63, 32, 32)
    draw_circle(display, 63, 32, 35)

    #draw numbers
    for n in range(1,13):
        draw_clock_num(display, 59, 30, 26, n)

    #draw arms:
    draw_mahog(display, hour, min, sec, 63, 32, 30)

    try:
        display.show()
    except:
        pass
    
    sleep(1)
