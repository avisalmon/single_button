# Lesson 100/110/111 — Pong Parts 2 & 3: Ball + Collision
**Videos:**  
- [100 pong part 2](https://www.youtube.com/watch?v=eEXuKzupk_w) (~1 min)  
- [110 functions](https://www.youtube.com/watch?v=29LO7Znncrg) (~6 min)  
- [111 pong collision](https://www.youtube.com/watch?v=B8l2I_6iC90) (~7 min)  
**Code:** `100 pong part 2.py`, `110 pong part 3 colision.py`

## Part 2 — Adding the Ball
Combine the bouncing ball from lesson 070 with the paddle from lesson 090.  
Both objects update in the same `while True` loop.

```python
# Draw both:
display.fill_rect(stick_pos_x, 50, 30, 5, 1)           # paddle
display.fill_rect(ball_x, ball_y, 10, 10, 1)            # ball
```

## Part 3 — Functions and Collision

### Why Functions?
A `def` wraps reusable logic and gives it a name.  
`collision()` checks if the ball overlaps the paddle — cleaner than inline conditionals.

```python
def collision():
    if player_position_y > 40 \
       and (player_position_x > stick_pos_x - 10 \
            and player_position_x < stick_pos_x + 30) \
       and player_speed_y > 0:
        return True
    return False
```

### Collision Response
```python
if collision():
    player_speed_y *= -1       # reverse vertical direction
    player_position_y -= 1     # nudge ball out to prevent sticking
```

### AABB Collision (Axis-Aligned Bounding Box)
Two rectangles overlap if:
```
ball_x < paddle_x + paddle_width   AND   ball_x + ball_width > paddle_x
ball_y < paddle_y + paddle_height  AND   ball_y + ball_height > paddle_y
```

## Complete Pong Loop
```
while True:
  1. Clear screen
  2. Draw paddle + ball
  3. Show
  4. Read button → update paddle position
  5. Update ball position
  6. Check wall collisions → reverse speed
  7. Check paddle collision → reverse Y speed
```

## Exercises
1. Make the game end (stop loop) when ball hits the bottom
2. Show the score on screen (how many times ball hit paddle)
3. Speed up ball slightly after each successful hit
