# **************************************************
# ESP32 Weather to OLED (HTTP only)
# By Avi Salmon
# **************************************************

import network
import urequests
import time
from machine import I2C, Pin
import ssd1306

# ----- OLED -----
display = None
try:
    i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
    display = ssd1306.SSD1306_I2C(128, 64, i2c)
except OSError as e:
    print("OLED not available:", e)

def show(text, x, y):
    if display:
        display.text(text, x, y)
    else:
        print(text)

def clear():
    if display:
        display.fill(0)

def flush():
    if display:
        display.show()

# ----- WiFi -----
ssid = "AviRedmi"
password = "aviaviavi"

def connect_wifi(ssid, password, retries=3):
    wlan = network.WLAN(network.STA_IF)
    last_error = None

    for _ in range(retries):
        try:
            if wlan.active():
                wlan.disconnect()
                wlan.active(False)
                time.sleep(0.3)

            wlan.active(True)
            time.sleep(0.3)
            wlan.connect(ssid, password)

            for _ in range(60):
                if wlan.isconnected():
                    return wlan, None
                time.sleep(0.2)

            last_error = "timeout"
        except OSError as e:
            last_error = e
            time.sleep(0.8)

    return wlan, last_error


wlan, wifi_error = connect_wifi(ssid, password)

clear()
if wifi_error is not None or not wlan.isconnected():
    show("WiFi FAILED", 0, 0)
    show(str(wifi_error)[:16], 0, 12)
    flush()
    raise SystemExit()
else:
    show("WiFi OK", 0, 0)
    flush()
    time.sleep(0.7)

# ----- Weather API (HTTP, NO HTTPS!) -----
URL = "http://wttr.in/Jerusalem?format=j1"   # JSON, HTTP only

clear()
show("Fetching weather...", 0, 0)
flush()

r = None
try:
    r = urequests.get(URL)
    data = r.json()

    curr = data["current_condition"][0]
    temp = curr["temp_C"]
    hum = curr["humidity"]
    desc = curr["weatherDesc"][0]["value"]

except Exception as e:
    clear()
    show("API ERROR", 0, 0)
    show(str(e)[:16], 0, 12)
    flush()
    raise SystemExit()
finally:
    if r is not None:
        r.close()

# ----- Display Weather -----
clear()
show("Jerusalem Weather", 0, 0)
show("Temp: {} C".format(temp), 0, 16)
show("Humidity: {}%".format(hum), 0, 28)
show(desc[:16], 0, 44)
flush()
