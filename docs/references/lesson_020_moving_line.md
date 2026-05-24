# Lesson 020/021/022 — Moving the Line & Performance
**Videos:**  
- [020 intro](https://www.youtube.com/watch?v=D2WSFFeNTw4) (~16 min)  
- [021 move the line](https://www.youtube.com/watch?v=s_1dilEqFfM) (~8 min)  
- [022 performance](https://www.youtube.com/watch?v=RELDbdn2RzU) (~7 min)  
**Code:** `020 move the line.py`

## What You Learn
- The **game loop** pattern: clear → draw → show → update (infinite `while True`)
- Using **variables** for position (`x`, `y`) and speed (`x_speed`, `y_speed`)
- **Boundary detection**: flip direction when hitting screen edge
- Direction reversal trick: `speed *= -1`
- **Performance**: raising I2C frequency from 400kHz → 4MHz dramatically improves frame rate
- `display.show()` is the bottleneck — it transfers the entire 1KB frame buffer

## Key Code Pattern
```python
x = 0
x_speed = 1

while True:
    display.fill(0)                    # 1. clear
    display.line(x, 0, 63, 63, 1)     # 2. draw
    display.show()                     # 3. push to screen
    x += x_speed                       # 4. update
    if x > 127 or x < 0:
        x_speed *= -1                  # reverse direction
```

## Performance Tip
```python
# Slow (default):
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)

# Fast (~10x faster):
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=4000000)
```

## Exercises
1. Make it faster (increase speed variable)
2. Flip — top of line stays fixed, bottom moves
3. Do something creative with the line
