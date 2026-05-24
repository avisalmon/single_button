# Lesson 050 — Read the Button
**Video:** [050 read a button](https://www.youtube.com/watch?v=lveNiPN7LF0) (~8.5 min)  
**Code:** `050 read button.py`

## What You Learn
- How to wire the button: one leg to **pin D4**, other leg to **GND**
- `Pin(4, Pin.IN, Pin.PULL_UP)` — enables internal pull-up resistor
- **Active-low logic**: button.value() returns `1` when NOT pressed, `0` when pressed
- Reading the value: `button.value()`
- Using `if/else` to branch on button state
- `sleep()` to pause execution

## Key Code
```python
from machine import Pin
from time import sleep

button = Pin(4, Pin.IN, Pin.PULL_UP)

# Read once:
if button.value() == 1:
    display_text("not pressed")
else:
    display_text("PRESSED!")

# Fill screen with button state:
while True:
    display.fill(button.value())   # 1=white (not pressed), 0=black (pressed)
    display.show()
```

## Why PULL_UP?
Without a pull-up, an unconnected pin floats and reads random values.  
`Pin.PULL_UP` connects an internal resistor to 3.3V, so:
- Button **open** → pin sees 3.3V → reads **1**
- Button **closed** (to GND) → pin is pulled low → reads **0**

## Exercises
1. Print your first name if button is pressed, family name if not
