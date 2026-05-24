# **************************************************
# ESP32 Weather to OLED (HTTP only)
# By Avi Salmon
# **************************************************

import network
import urequests
import time
from machine import SoftI2C, Pin
import ssd1306

# ----- OLED -----
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

def show(text, x, y):
    display.text(text, x, y)

def clear():
    display.fill(0)

# ----- WiFi -----
ssid = "AviRedmi"
password = "aviaviavi"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

for _ in range(40):
    if wlan.isconnected():
        break
    time.sleep(0.2)

clear()
if not wlan.isconnected():
    show("WiFi FAILED", 0, 0)
    display.show()
    raise SystemExit()
else:
    show("WiFi OK", 0, 0)
    display.show()
    time.sleep(0.7)

# ----- Weather API (HTTP, NO HTTPS!) -----
URL = "http://wttr.in/Jerusalem?format=j1"   # JSON, HTTP only

clear()
show("Fetching weather...", 0, 0)
display.show()

try:
    r = urequests.get(URL)
    data = r.json()
    r.close()

    curr = data["current_condition"][0]
    temp = curr["temp_C"]
    hum = curr["humidity"]
    desc = curr["weatherDesc"][0]["value"]

except Exception as e:
    clear()
    show("API ERROR", 0, 0)
    show(str(e)[:16], 0, 12)
    display.show()
    raise SystemExit()

# ----- Display Weather -----
clear()
show("Jerusalem Weather", 0, 0)
show("Temp: {} C".format(temp), 0, 16)
show("Humidity: {}%".format(hum), 0, 28)
show(desc[:16], 0, 44)
display.show()
