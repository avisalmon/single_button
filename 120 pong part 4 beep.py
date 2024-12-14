# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on https://github.com/avisalmon/single_button
#
# Pong 4: Beep
# ****************************************

from machine import Pin, I2C, PWM
import ssd1306
from font import Font
from time import sleep, ticks_ms

#setting the buzzer:
from time import sleep_ms
buzzer_pin = Pin(23, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)

def buzz(duration_ms, frequency):
    buzzer_pwm.freq(frequency)  # Set the PWM frequency
    buzzer_pwm.duty(512)        # Set the PWM duty cycle (50% for a beep)
    sleep_ms(duration_ms)
    buzzer_pwm.duty(0)

buzz(500, 880)
sleep_ms(1000)
# musical notes frequencies:
#        C4: 261.63 Hz
#        C#4 / Db4: 277.18 Hz
#        D4: 293.66 Hz
#        D#4 / Eb4: 311.13 Hz
#        E4: 329.63 Hz
#        F4: 349.23 Hz
#        F#4 / Gb4: 369.99 Hz
#        G4: 392.00 Hz
#        G#4 / Ab4: 415.30 Hz
#        A4: 440.00 Hz
#        A#4 / Bb4: 466.16 Hz
#        B4: 493.88 Hz
# we can play i.e. like this

song=[(500, 261), (500,293), (500, 329), (500,349), (500, 392)]
for duration, freq in song:
    buzz(duration, freq)

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

button = Pin(4, Pin.IN, Pin.PULL_UP)

stick_pos_x = 50
player_position_x = 0
player_position_y = 0
player_speed_x = 1
player_speed_y = 2

last_button_status = 0
direction = 1 # 1 is right, -1 is left

def collision():
    if player_position_y > 40 \
           and (player_position_x > stick_pos_x - 10 and player_position_x < stick_pos_x + 30) \
           and player_speed_y > 0:
        buzz(50, 880)
        return True
    return False

while True:
    # clear the screen
    display.fill(0)
    
    #draw the stick and ball
    display.fill_rect(stick_pos_x, 50, 30, 5 , 1)
    display.fill_rect(player_position_x, player_position_y, 10, 10 , 1)
    display.show()
    
    button_pressed = not button.value()
    
    # calculate new stick position:
    if button_pressed: # button is pressed
        if last_button_status == 0:
            direction *= -1
        last_button_status = 1
        
        stick_pos_x += 5 * direction
        
    else:
        last_button_status = 0
        
    # calculate new player position:
    player_position_x += player_speed_x
    player_position_y += player_speed_y
    # if collision jump up. 
    if collision():
        player_speed_y *= -1
        player_position_y -= 1
        
    if player_position_x > 127 or player_position_x < 0 :
        player_speed_x *= -1
    if player_position_y > 63 or player_position_y < 0:
        player_speed_y *= -1
    
# You now have the tools to add points and see if the player loose.
# There may be some bugs in this game as it is writte. manage with it... 