import machine
from machine import Pin, PWM
import ssd1306
import time
import urandom

# Initialize I2C for OLED
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

from time import sleep_ms
buzzer_pin = Pin(23, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)

# Initialize buttons and buzzer
buttons = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_UP) for i in [4,2]]
print(buttons)

SOUND = [440, 1200]

# Function to play sound
def play_sound(button_index):
    buzzer_pwm.freq(SOUND[button_index])  # Set the PWM frequency
    buzzer_pwm.duty(512)        # Set the PWM duty cycle (50% for a beep)
    sleep_ms(500)
    buzzer_pwm.duty(0)

# Function to display score
def display_score(score):
    oled.fill(0)
    oled.text('Simon Game ', 10, 10)
    oled.text('Score: {}'.format(score), 10, 30)
    oled.show()
    
def read_button():
    in_read = -1
    # wait for key:
    while in_read == -1:
        sleep_ms(100)
        vals = [buttons[n].value() for n in range(2)]
        #print(vals)
        if 0 in vals:
            print(1)
            in_read = vals.index(0)
    pressed_button = in_read
    print(pressed_button)
    # buz and wait until clear
    sleep_ms(100)
    buzzer_pwm.freq(SOUND[in_read])
    buzzer_pwm.duty(512)
    while in_read != -1:
        vals = [buttons[n].value() for n in range(2)]
        if 0 not in vals:
            in_read = -1
            buzzer_pwm.duty(0)
    
    return pressed_button

# Main game logic
def play_simon_game():
    for n in range(2):
        play_sound(n)
        
 
    time.sleep(1)    
    
    sequence = []
    game_on = True
    while game_on:
        sequence.append(urandom.randint(0, 1))
        print(sequence)
        for index in sequence:
            play_sound(index)
            time.sleep(0.5)
        
        print('Here')
        for index in sequence:
            if read_button() != index:
                game_on = False
                for fr in [880, 440, 220, 110]:
                    buzzer_pwm.freq(fr)
                    buzzer_pwm.duty(512)
                    sleep_ms(300)
                buzzer_pwm.duty(0)
            
        display_score(len(sequence))
        time.sleep(1)
    

# Run the game
play_simon_game()

