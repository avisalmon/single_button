# Lesson 070 — Move Around
**Video:** [070 move around](https://www.youtube.com/watch?v=tVNSqr0vF4g) (~5.5 min)  
**Code:** `070 move around.py`

## What You Learn
- Creating a **player object** with position and speed variables
- Drawing a player as a filled rectangle: `display.fill_rect(x, y, w, h, c)`
- **2D boundary detection** — checking both X and Y edges
- Game loop with full player state update each frame

## Key Code
```python
player_x = 0
player_y = 0
speed_x  = 1
speed_y  = 2

while True:
    display.fill(0)
    display.fill_rect(player_x, player_y, 10, 10, 1)   # draw 10×10 square
    display.show()

    player_x += speed_x
    player_y += speed_y

    if player_x > 127 or player_x < 0:
        speed_x *= -1
    if player_y > 63 or player_y < 0:
        speed_y *= -1
```

## Concept: Sprite Boundary
The `fill_rect` starts at (x, y) and extends right/down by width/height.  
To keep it fully on screen: `x` must stay between `0` and `127 - width`.

## Exercises
1. Make the player go **only horizontally** (remove Y movement)
2. Make the player **thin and wide** (e.g. 40×5 instead of 10×10)
