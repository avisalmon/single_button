"""
Simple Servo Sweep Program for ESP32 using MicroPython
This program controls a single servo motor and makes it sweep back and forth
to test if the servo is working correctly.
"""

from machine import Pin, PWM
import time

# Servo Configuration
# Define servo pin (using pins from the other side of the ESP32)
servo_pin = 18  # Using pin 18 from the other side

# Create PWM object for the servo
servo = PWM(Pin(servo_pin), freq=50)

# Button for controlling the servo (using the single button approach)
button = Pin(0, Pin.IN, Pin.PULL_UP)

# Current position of servo (angle in degrees)
servo_pos = 90
sweep_active = False

# Helper function to convert angle to PWM duty cycle
def angle_to_duty(angle):
    """Convert angle in degrees (0-180) to duty cycle"""
    # Most servo motors expect PWM signal with period of 20ms (freq=50Hz)
    # Pulse width between 1ms (duty=5%) and 2ms (duty=10%)
    min_duty = 26  # ~1ms pulse (0 degrees)
    max_duty = 123  # ~2ms pulse (180 degrees)
    return min_duty + (max_duty - min_duty) * (angle / 180)

# Set servo position
def set_servo_position():
    servo.duty(int(angle_to_duty(servo_pos)))

# Function to sweep servo back and forth
def sweep_servo():
    global servo_pos
    
    # Sweep from 0 to 180 degrees
    for angle in range(0, 180, 5):
        servo_pos = angle
        set_servo_position()
        time.sleep(0.05)
    
    # Sweep from 180 to 0 degrees
    for angle in range(180, 0, -5):
        servo_pos = angle
        set_servo_position()
        time.sleep(0.05)

# Button debouncing variables
last_press_time = 0
debounce_time = 200  # milliseconds

# Main control loop
def main():
    global sweep_active, servo_pos, last_press_time
    
    # Initialize servo position
    set_servo_position()
    print("Servo Sweep Test Program")
    print("Press the button to start/stop sweeping")
    
    while True:
        current_time = time.ticks_ms()
        button_value = button.value()
        
        # Button pressed (active low)
        if button_value == 0:
            # Debounce
            if time.ticks_diff(current_time, last_press_time) > debounce_time:
                # Toggle sweep mode
                sweep_active = not sweep_active
                print("Sweep mode: {}".format("ON" if sweep_active else "OFF"))
                last_press_time = current_time
        
        # Run sweep if active
        if sweep_active:
            sweep_servo()
        
        # Brief pause to prevent hogging the CPU
        time.sleep(0.01)

# Start the program
if __name__ == "__main__":
    print("Starting Servo Sweep Test Program")
    main()