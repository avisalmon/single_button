# Lesson 090 — Pong Part 1: The Paddle
**Video:** [090 pong 1](https://www.youtube.com/watch?v=zeDq5jQDPiw) (~8 min)  
**Code:** `090 pong part 1.py`  
**Subtitles:** `12 090 pong 1.en.vtt` ✓

## What You Learn
- How to control the paddle with **a single button**
- **Edge detection**: distinguish a new button press from holding it down
- Direction toggle: each new press reverses paddle direction
- Combining button input with position update in the game loop

## The Single-Button Control Pattern
The button has only two states (pressed / not pressed). To get more control:
- Each **new press** (edge) reverses the movement direction
- While **held**, paddle keeps moving in current direction

```python
last_button_status = 0
direction = 1   # 1 = right, -1 = left

while True:
    button_pressed = not button.value()   # active-low

    if button_pressed:
        if last_button_status == 0:       # NEW press (edge)
            direction *= -1               # reverse direction
        last_button_status = 1
        stick_pos_x += 5 * direction      # move paddle
    else:
        last_button_status = 0            # reset edge detector
```

## Key Insight: Edge Detection
```
Button state:  0  0  1  1  1  0  0  1  1  0
last_status:   0  0  0  1  1  0  0  0  1  0
Edge (new press):        ↑              ↑
```
The edge fires only on the **rising edge** (transition from 0→1).

## Exercises
1. Make the paddle move faster when held
2. Prevent the paddle from going off the edges of the screen
