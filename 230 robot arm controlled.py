"""
Simple Web Server for ESP32 using MicroPython
This program creates a web server that accepts REST commands and displays them on an OLED screen.
"""

import socket
import network
import time
from machine import Pin, I2C
import ssd1306

# Wi-Fi Configuration
WIFI_SSID = "YourWiFiSSID"  # Replace with your Wi-Fi SSID
WIFI_PASSWORD = "YourWiFiPassword"  # Replace with your Wi-Fi password

# Server Configuration
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 80  # Standard HTTP port

# OLED Display Setup (as seen in 010 lines.py)
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.text("Server starting...", 0, 0)
display.show()

# Connect to Wi-Fi network
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print(f"Connecting to {WIFI_SSID}...")
        display.fill(0)
        display.text(f"Connecting to", 0, 0)
        display.text(f"{WIFI_SSID}...", 0, 10)
        display.show()
        
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        
        # Wait for connection with timeout
        timeout = 20
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
    
    if wlan.isconnected():
        ip, subnet, gateway, dns = wlan.ifconfig()
        print(f"Connected to {WIFI_SSID}")
        print(f"IP address: {ip}")
        
        display.fill(0)
        display.text("Connected!", 0, 0)
        display.text(f"IP: {ip}", 0, 10)
        display.show()
        
        return ip
    else:
        print("Failed to connect to WiFi")
        # Fall back to AP mode
        return start_ap_mode()

# Start Access Point mode if unable to connect to WiFi
def start_ap_mode():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid='ESP32Server', password='esp32pass')
    
    ip = ap.ifconfig()[0]
    print("Started Access Point: ESP32Server")
    print(f"Password: esp32pass")
    print(f"IP address: {ip}")
    
    display.fill(0)
    display.text("AP Mode:", 0, 0)
    display.text("ESP32Server", 0, 10)
    display.text(f"Pass: esp32pass", 0, 20)
    display.text(f"IP: {ip}", 0, 30)
    display.show()
    
    return ip

# Display received command on OLED
def display_command(command):
    display.fill(0)
    display.text("Command received:", 0, 0)
    
    # Split command into multiple lines if needed
    if len(command) > 16:  # If command is long, split it
        for i in range(0, len(command), 16):
            line = command[i:i+16]
            line_num = (i // 16) + 1
            if line_num <= 5:  # Display up to 5 lines (0-4 + header)
                display.text(line, 0, line_num * 10)
    else:
        display.text(command, 0, 10)
    
    display.text("REST API active", 0, 50)
    display.show()

# Parse HTTP request
def parse_request(request):
    # Basic HTTP request parsing
    request_lines = request.split(b'\r\n')
    request_line = request_lines[0].decode('utf-8')
    method, path, _ = request_line.split(' ', 2)
    return method, path

# Handle HTTP requests
def handle_request(client_socket):
    try:
        # Receive data from client
        request = client_socket.recv(1024)
        if not request:
            return

        # Parse the request
        method, path = parse_request(request)
        print(f"Received: {method} {path}")
        
        # Extract command from path
        if path.startswith('/cmd/'):
            command = path[5:]  # Remove '/cmd/' prefix
            display_command(command)
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nCommand received: " + command
        elif path == '/':
            # Serve a simple HTML page with instructions
            html = """<!DOCTYPE html>
<html>
<head>
    <title>ESP32 REST Command Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial; padding: 20px; text-align: center; }
        .container { max-width: 500px; margin: 0 auto; }
        input, button { padding: 10px; margin: 10px; }
        #commandInput { width: 80%; }
    </style>
</head>
<body>
    <div class="container">
        <h1>ESP32 REST Command Server</h1>
        <p>Send commands to display on the OLED screen:</p>
        
        <input type="text" id="commandInput" placeholder="Enter command">
        <button onclick="sendCommand()">Send</button>
        
        <div id="response" style="margin-top: 20px;"></div>
        
        <h2>REST API:</h2>
        <p>Send commands to: <code>/cmd/your-command-here</code></p>
    </div>
    
    <script>
        function sendCommand() {
            const command = document.getElementById('commandInput').value;
            if (!command) return;
            
            const url = '/cmd/' + encodeURIComponent(command);
            fetch(url)
                .then(response => response.text())
                .then(data => {
                    document.getElementById('response').innerText = data;
                })
                .catch(error => {
                    document.getElementById('response').innerText = 'Error: ' + error;
                });
        }
    </script>
</body>
</html>
"""
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
        else:
            # 404 Not Found for any other paths
            response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nNot Found"

        # Send response
        client_socket.send(response.encode('utf-8'))
            
    except Exception as e:
        print(f"Error handling request: {e}")
    finally:
        # Close the connection
        client_socket.close()

# Main function
def main():
    # Connect to WiFi or start AP
    ip_address = connect_wifi()
    
    # Create socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Server started at http://{ip_address}:{PORT}")
        
        display.fill(0)
        display.text("Server ready!", 0, 0)
        display.text(f"IP: {ip_address}", 0, 10)
        display.text("Waiting for", 0, 30)
        display.text("commands...", 0, 40)
        display.show()
        
        while True:
            # Accept client connection
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            
            # Handle the request
            handle_request(client_socket)
            
    except Exception as e:
        print(f"Server error: {e}")
        display.fill(0)
        display.text("Server error:", 0, 0)
        display.text(str(e)[:16], 0, 10)
        display.show()
    finally:
        server_socket.close()
        print("Server stopped")

# Start the program
if __name__ == "__main__":
    print("Starting REST Command Server")
    main()
