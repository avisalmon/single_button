# ****************************************
#
# Learning Micro Python and programming with ESP32
# By: Avi Salmon
# All instructions on https://github.com/avisalmon/single_button
#
# Game Demo - Space invadors. 
# ****************************************

from machine import Pin, I2C, PWM
import ssd1306
from font import Font
from time import sleep, ticks_ms
from time import sleep_ms
import _thread as th

# Buzzer:
buzzer_pin = Pin(23, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.duty(0)

def buzz(duration_ms, frequency):
    buzzer_pwm.freq(frequency)  # Set the PWM frequency
    buzzer_pwm.duty(200)        # Set the PWM duty cycle (50% for a beep)
    sleep_ms(duration_ms)
    buzzer_pwm.duty(0)

#button:
button = Pin(4, Pin.IN, Pin.PULL_UP)

#screen:
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000) 
display = ssd1306.SSD1306_I2C(128, 64, i2c)  # display object
f=Font(display)

game_tick = 0
game_on = True

def game_timing():
    ticking_time = 1000
    freq = 200
    global game_tick
    global game_on
    while game_on:
        sleep_ms(ticking_time)
        game_tick = 1
        buzz(2,freq)
        freq += 50
        if ticking_time > 100:
            ticking_time -= 10

th.start_new_thread(game_timing, ())

class Invador:
    def __init__(self, x_pos, y_pos, size=8):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
        self.image = 1
        
    def draw(self, y_offset):
        display.fill_rect(self.x_pos, self.y_pos + y_offset, self.size, self.size , 1)
        
    def check_collide(self, x, y, ext_size):
        if ((self.x_pos < x < self.x_pos + self.size) and (self.y_pos < y < self.y_pos + self.size)) or ((self.x_pos < x+ext_size < self.x_pos + self.size) and (self.y_pos < y+ext_size < self.y_pos + self.size)):
            return True
        else:
            return False
            
    
    def __str__(self):
        return f'Invador {self.x_pos} x {self.y_pos}'
    
class Player:
    def __init__(self, x_pos = 60, y_pos = 55):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.misile = False
        self.misile_x = 0
        self.misile_y = 0
        self.step = 4
        self.moving = False
        
    def draw(self):
        display.rect(self.x_pos, self.y_pos, 20, 5, 1)
        if self.misile:
            display.rect(self.misile_x, self.misile_y, 2, 2, 1)
            self.misile_y -= 2
            if self.misile_y < 0:
                self.misile = False

    def move(self):
        if button.value() == 0:
            if not self.moving:
                self.moving = True
            self.x_pos += self.step
            if self.x_pos < 0 or self.x_pos > 122:
                self.step *= -1
        else:
            if self.moving == True:
                self.shoot()
                self.moving = False
    
    def shoot(self):
        if not self.misile:
            print('shoot')
            self.misile = True
            self.misile_x = self.x_pos + 10
            self.misile_y = self.y_pos
    
# Create invador
start_x = 50
start_y = 0
y_offset = 0
space = 10
invadors = []
for j in range(3):
    for k in range(8):
        invadors.append(Invador(start_x + k*space, start_y + j*space))
        
#create player
player = Player()
    
stepping = -5

while game_on:
    display.fill(0)
    if game_tick:
        # check for boundaries:
        for invador in invadors:
            if invador.x_pos < 0 or invador.x_pos > 122:
                stepping *= -1
                y_offset += 3
                break
        
        # move all invadors
        for invador in invadors:
            invador.x_pos += stepping

        game_tick = 0
    
    for invador in invadors:
        if invador.y_pos + y_offset > 45:
            game_on = False
        invador.draw(y_offset)
        
    if player.misile:
        for invador in invadors[:]: # the [:] create a copy of the list so I can now remove items from the original list
            if invador.check_collide(player.misile_x, player.misile_y, 2):
                invadors.remove(invador)
                player.misile = False
                break
    
    if len(invadors) == 0:
        print('end')
        game_on = False
            
    player.move()
    player.draw()
    display.show()
    
display.fill(0)
if len(invadors) == 0:
    display.text('Winner', 20, 20, 1)
else:
    display.text('Lost', 20, 20, 1)
display.show()
