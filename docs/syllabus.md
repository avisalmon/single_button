# הצעת תכנית לימודים — תכנות עם MicroPython וערכת ESP32

**מאת: אבי סלמון**  
פלטפורמה: ESP32 + מסך OLED SSD1306 (128×64) + כפתור אחד  
קוד המקור: [github.com/avisalmon/single_button](https://github.com/avisalmon/single_button)

---

## Overview

This course teaches programming from first principles using an ESP32 microcontroller, a small OLED screen, and a single push-button. Students learn MicroPython, hardware interfacing, game design, and real-world IoT concepts by building progressively more complex projects — from drawing a line to a fully animated Space Invaders game and a WiFi-connected clock.

---

## Prerequisites

- None. No prior programming experience required.
- A computer with Thonny IDE installed.
- An ESP32 board with SSD1306 OLED display and one push-button wired to pin D4.

---

## Module 1 — Drawing on Screen

### Lesson 1 — Lines (`010 lines.py`)
**Concepts:** Setting up I2C, initializing the OLED display, coordinate system (128×64), drawing a line, clearing the screen.  
**Key functions:** `I2C()`, `SSD1306_I2C()`, `display.fill()`, `display.line()`, `display.show()`  
**Exercises:**
1. Draw a big X on the screen.
2. Draw the third letter of your name.

---

### Lesson 2 — Moving the Line (`020 move the line.py`)
**Concepts:** Variables, the `while True` game loop, speed variables, bouncing logic (reversing direction at boundaries).  
**New ideas:** Animation loop, state in variables, `if` conditions for boundary detection.  
**Exercises:**
1. Make the animation faster.
2. Flip the direction — keep the top endpoint still, move the bottom.
3. Do something creative with the line.

---

### Lesson 3 — More Drawing Primitives (`030 more than lines.py`)
**Concepts:** Full drawing toolkit — pixels, horizontal/vertical lines, rectangles (outline and filled), scrolling, built-in text.  
**Key functions:** `display.pixel()`, `display.hline()`, `display.vline()`, `display.rect()`, `display.fill_rect()`, `display.text()`  
**Exercises:**
1. Draw a bold square with both diagonals.

---

## Module 2 — Text and Input

### Lesson 4 — Text and Custom Fonts (`040 text.py`)
**Concepts:** Built-in 8×8 font, custom `Font` library, multi-size text (8, 16, 24, 32 px), text positioning.  
**New ideas:** Importing custom modules (`font.py`), scaling UI elements.  
**Exercises:**
1. Write your name large and your phone number small.

---

### Lesson 5 — Reading the Button (`050 read button.py`)
**Concepts:** GPIO input, `Pin.PULL_UP` (logic is inverted), polling a button in a loop, conditional display based on button state.  
**Key functions:** `Pin(4, Pin.IN, Pin.PULL_UP)`, `button.value()`  
**Exercises:**
1. Print your first name when the button is pressed, family name when released.

---

## Module 3 — Sprites and Movement

### Lesson 6 — Blit and FrameBuffer (`060 blit.py`)
**Concepts:** Off-screen drawing with `FrameBuffer`, compositing sprites onto the display using `blit`, transparency key parameter.  
**Key functions:** `framebuf.FrameBuffer()`, `display.blit()`, `display.fill_rect()`  
**Why it matters:** Efficient sprite rendering — draw once, stamp many times.

---

### Lesson 7 — Single Player Movement (`070 move around.py`)
**Concepts:** Player position and speed variables, bouncing off all four walls, rendering a moving rectangle.  
**Pattern:** Clear → Draw → Update → Repeat.  
**Exercises:**
1. Make the player move only horizontally.
2. Make the player thin and wide (a paddle shape).

---

### Lesson 8 — Object-Oriented Programming (`080 few players.py`)
**Concepts:** Classes, `__init__`, instance variables, methods (`move()`), creating multiple objects in a list, iterating with `for`.  
**New ideas:** OOP as a way to manage multiple independent game entities.  
**Result:** Four bouncing squares, each with its own speed and position, using one `Player` class.

---

## Module 4 — Pong (4-Part Project)

### Pong Part 1 — The Paddle (`090 pong part 1.py`)
**Concepts:** Button-controlled movement, direction toggling (press changes direction), hold-to-move pattern using `last_button_status`.  
**Result:** A paddle that moves left or right when the button is held; reverses direction on each new press.

---

### Pong Part 2 — The Ball (`100 pong part 2.py`)
**Concepts:** Combining button-controlled paddle with a bouncing ball on the same screen.  
**Result:** Paddle and ball coexist — full Pong layout without collision yet.

---

### Pong Part 3 — Collision Detection (`110 pong part 3 colision.py`)
**Concepts:** Writing a `collision()` function, checking overlapping rectangles using coordinate math, reversing ball direction on hit.  
**Key pattern:** Separate collision logic into its own function; check position ranges with `and` conditions.  
**Result:** The ball bounces off the paddle — playable Pong.

---

### Pong Part 4 — WiFi and Weather API (`120 pong part 4 beep.py`)
**Concepts:** Connecting to WiFi with `network.WLAN`, making HTTP GET requests with `urequests`, parsing JSON, displaying live weather data.  
**Key functions:** `wlan.connect()`, `urequests.get()`, `r.json()`  
**Result:** ESP32 fetches real-time weather for Jerusalem and displays temperature, humidity, and description on the OLED.

---

## Module 5 — Advanced Games

### Snake with Threading and Timers (`130 smake.py`)
**Concepts:** `_thread` for concurrent button reading, `Timer` for periodic events (snake growth), PWM buzzer for sound, `random` module, list manipulation for a growing snake body, game state management.  
**New ideas:** Multi-threading on a microcontroller, hardware timers, interrupt-driven input.  
**Result:** A working Snake game on a 13×7 grid with sound.

---

### Simon Memory Game (`140 simon.py`)
**Concepts:** Two buttons, PWM buzzer with different frequencies per button, random sequence generation, reading and validating player input, score display, game-over sound sequence.  
**Key patterns:** `urandom.randint()`, blocking input read with buzzer feedback, comparing player sequence to stored sequence.  
**Result:** A full Simon Says memory game.

---

## Module 6 — Space Invaders (2-Part Project)

### Space Invaders — Basic (`150 space.py`)
**Concepts:** OOP with `Invador` and `Player` classes, threading for game timing, missile mechanics (shoot on button release), collision detection between missile and invaders, list copy (`[:]`) for safe removal during iteration, escalating difficulty (speed increases over time).  
**Result:** A playable Space Invaders clone with shooting, multiple enemies, and a player that loses if invaders reach the bottom.

---

### Space Invaders — Animated Sprites (`170 space animated.py`)
**Concepts:** Loading sprite images from binary files (`.bin`), multi-frame animation (sprite sheets), `Sprite` base class from `singame` module, frame cycling with `next_frame()`, two concurrent timer threads (game tick + animation tick).  
**New ideas:** Inheritance (`Invador` extends `Sprite`), asset-based graphics, separating animation rate from game logic rate.  
**Result:** Space Invaders with animated alien sprites.

---

## Module 7 — IoT and Real-World Applications

### Analog Clock with NTP (`210 watch example.py`)
**Concepts:** WiFi connection, NTP time synchronization (`ntptime.settime()`), UTC timezone adjustment, tracking time with `ticks_ms()` to avoid repeated sync, trigonometry (`sin`, `cos`, `pi`) for clock hand angles, drawing clock face with numbers.  
**Key patterns:** Sample real time once, track elapsed ms locally for smooth updates; convert between angle degrees and display coordinates.  
**Result:** A real-time analog clock that fetches the correct time from the internet and renders hour, minute, and second hands on the OLED.

---

## Skills Progression Summary

| Module | Skills Introduced |
|--------|-------------------|
| 1 | Hardware setup, coordinate system, animation loop, variables |
| 2 | GPIO input, button polling, custom fonts, conditional logic |
| 3 | Sprites, FrameBuffer, OOP (classes and instances) |
| 4 | Game mechanics: paddle, ball, collision, WiFi/HTTP/JSON |
| 5 | Multi-threading, timers, buzzer (PWM), random, complex game logic |
| 6 | Inheritance, sprite animation, asset loading, escalating difficulty |
| 7 | NTP/WiFi IoT, trigonometry, real-time data display |

---

## Final Projects (Student Choice)

By the end of the course, students have the tools to build:

- A reaction-time game (button + timer)
- A scrolling message board (WiFi + text display)
- A temperature/humidity monitor (sensor + OLED)
- Their own original game using the patterns from all modules

---

*All source files: [github.com/avisalmon/single_button](https://github.com/avisalmon/single_button)*
