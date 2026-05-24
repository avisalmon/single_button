# Lesson 030 — More Than Lines
**Video:** [030 more than lines](https://www.youtube.com/watch?v=Z9-u8Ub67hw) (~3 min)  
**Code:** `030 more than lines.py`

## What You Learn
All the drawing primitives beyond `line()`:

| Method | Description |
|--------|-------------|
| `display.pixel(x, y, c)` | Set a single pixel |
| `display.hline(x, y, w, c)` | Horizontal line of width `w` |
| `display.vline(x, y, h, c)` | Vertical line of height `h` |
| `display.rect(x, y, w, h, c)` | Rectangle outline |
| `display.fill_rect(x, y, w, h, c)` | Filled rectangle |
| `display.text(str, x, y, c)` | Built-in 8px font text |
| `display.scroll(dx, dy)` | Scroll the screen buffer |

## Key Code
```python
display.fill(0)
display.pixel(3, 10, 1)             # single pixel
display.hline(0, 8, 40, 1)          # horizontal line
display.vline(0, 8, 10, 1)          # vertical line
display.rect(10, 10, 30, 30, 1)     # rectangle outline
display.text('Hello World', 0, 0, 1)
display.show()
```

## Exercises
1. Draw a **bold square** with diagonal lines inside it
