# Lesson 040 — Text
**Video:** [040 text](https://www.youtube.com/watch?v=AwkKSgIKmt0) (~3.5 min)  
**Code:** `040 text.py`

## What You Learn
- Built-in `display.text()` gives 8px-tall characters (very small)
- The custom `Font` class (from `font.py` on the device) supports bigger sizes
- Available font sizes: **8, 16, 24, 32** pixels tall
- Larger text needs more horizontal space — plan your layout

## Key Code
```python
from font import Font

f = Font(display)

# Built-in (8px):
display.text('First Line', 0, 0, 1)

# Custom font:
f.text("Hi", 0, 30, 16)    # 16px
f.text("Hi", 0, 10, 24)    # 24px
f.text("Hi", 0, 0,  32)    # 32px — only fits a few chars wide
```

## Font Size Guide
| Size | Height | Max chars across 128px |
|------|--------|------------------------|
| 8px  | 8      | 16 chars |
| 16px | 16     | 8 chars  |
| 24px | 24     | 5 chars  |
| 32px | 32     | 4 chars  |

## Exercises
1. Write your first name in 32px and your phone number in 8px below it
