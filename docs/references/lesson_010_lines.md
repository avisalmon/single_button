# Lesson 010 — Lines
**Video:** [010 lines](https://www.youtube.com/watch?v=VOU1evNbYDQ) (~17 min)  
**Code:** `010 lines.py`

## What You Learn
- How to connect the OLED display via I2C (pins SCL=22, SDA=21)
- How to create a display object: `ssd1306.SSD1306_I2C(128, 64, i2c)`
- The screen coordinate system: top-left is (0,0), bottom-right is (127,63)
- Drawing a line: `display.line(x1, y1, x2, y2, color)`
- Clearing the screen: `display.fill(0)`
- Sending the buffer to screen: `display.show()`
- Colors: `0` = black (off), `1` = white (on)

## Key Code Pattern
```python
from machine import Pin, I2C
import ssd1306

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.fill(0)                        # clear
display.line(30, 10, 50, 50, 1)        # draw line
display.show()                         # push to screen
```

## Screen Layout
```
(0,0)  ─────────────────  (127,0)
  │                              │
  │         128 × 64             │
  │                              │
(0,63) ─────────────────  (127,63)
```

## Exercises
1. Draw a big **X** on the screen (two lines crossing corner to corner)
2. Draw the third letter of your name using lines only
