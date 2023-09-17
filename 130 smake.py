# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on github/avisalmon/TBD
#
# Lesson 1: Pong 4: Snake + IRQ
# ****************************************

from machine import Pin, I2C, PWM, Timer
import machine
import ssd1306
from font import Font
from time import sleep, ticks_ms
import random
import _thread as th

#setting the buzzer:
from time import sleep_ms
buzzer_pin = Pin(23, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.duty(0)

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

direction_state = 0

button = Pin(4, Pin.IN, Pin.PULL_UP)

stick_pos_x = 50
player_position_x = 0
player_position_y = 0
player_speed_x = 1
player_speed_y = 2

def buzz(duration_ms, frequency):
    buzzer_pwm.freq(frequency)  # Set the PWM frequency
    buzzer_pwm.duty(512)        # Set the PWM duty cycle (50% for a beep)
    sleep_ms(duration_ms)
    buzzer_pwm.duty(0)

# split the screen to 13 x 7 squers 

direction = [(1, 0), (0,1), (-1,0), (0, -1)] # 0 right, 1 down, 2 left, 3 up 
direction_state = 0
snake=[(random.randint(0,24), random.randint(0,12))]
time_to_grow = 0

def draw_snake():
    for cube_x, cube_y in snake:
        display.fill_rect(cube_x * 5, cube_y * 5, 5, 5 , 1)
   
def move_snake():
    global time_to_grow
    last_element = snake[0]
       
    for n in range(len(snake)-1):
        snake[n] = snake[n+1]
        
    snake[-1] = (snake[-1][0] + direction[direction_state][0], snake[-1][1] + direction[direction_state][1])
    if time_to_grow:
        snake.insert(0, last_element)
        time_to_grow = 0

def grow_snake():
    global time_to_grow
    time_to_grow = 1
        
def button_event():
    while True:
        global direction_state

        if button.value()==0:
            if direction_state == 3:
                direction_state = 0
            else:
                direction_state += 1
            print(direction_state)
            sleep(0.3)

        
# use threads
th.start_new_thread(button_event,())

# use timer
tim1 = Timer(1)
tim1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:grow_snake())

timer = machine.Timer(-1)

while True:
    
    display.fill(0)
    draw_snake()
    display.show()
    
    # move the snake
    move_snake()
    sleep_ms(200)
 