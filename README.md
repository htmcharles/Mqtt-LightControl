# MQTT Light Control Project

A simple IoT project that demonstrates MQTT communication between a web interface and a simulated IoT device. Control a virtual light bulb from your browser and see real-time updates in a Python terminal.

![MQTT Light Control](https://i.imgur.com/example-image.jpg)

## Project Overview

This project consists of two main components:

1. **Web Interface (index.html)**: A browser-based UI with ON/OFF buttons to control a virtual light
2. **Simulated IoT Device (light_simulation.py)**: A Python script that simulates an IoT device (like an ESP8266)

Both components communicate via MQTT (Message Queuing Telemetry Transport), a lightweight messaging protocol designed for IoT applications.

## Features

- Modern, responsive web interface with dark mode support
- Real-time communication between web browser and Python script
- Visual feedback with animated light bulb
- Connection status indicators
- Detailed error handling and reporting

## Prerequisites

Before running this project, you need:

1. **Python 3.6+** with the following packages:
   - `paho-mqtt` (MQTT client for Python)

2. **Web Browser** (Chrome, Firefox, Edge, etc.)

3. **HiveMQ Account** (Optional - already configured with test account)
   - The project is pre-configured with test credentials
   - For your own setup, create an account at [HiveMQ Cloud](https://www.hivemq.com/cloud/)

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/mqtt-light-control.git
   cd mqtt-light-control
   ```

2. **Install Python dependencies**:
   ```
   pip install paho-mqtt
   ```

## Running the Project

### Step 1: Start the Simulated IoT Device

1. Open a terminal/command prompt
2. Navigate to the project directory
3. Run the Python script:
   ```
   python light_simulation.py
   ```
4. You should see:
   ```
   Connecting to broker 54d38e6010684c31a4d8ac17a897978b.s1.eu.hivemq.cloud on port 8884...
   Waiting for messages on topic /charles/light_control...
   ```

### Step 2: Open the Web Interface

1. Open the `index.html` file in your web browser:
   - Double-click the file, or
   - Drag and drop it into your browser, or
   - Use a local server if you have one

2. You should see the light control interface with:
   - A light bulb visualization
   - ON and OFF buttons
   - Connection status indicator

### Step 3: Control the Light

1. Click the "Turn ON" button in the web interface
   - The light bulb in the browser will turn on
   - The Python terminal will show: "💡 Light is TURNED ON"

2. Click the "Turn OFF" button in the web interface
   - The light bulb in the browser will turn off
   - The Python terminal will show: "💡 Light is TURNED OFF"

## How It Works

### Web Interface (index.html)

The web interface uses:
- MQTT.js to connect to the HiveMQ broker via WebSockets
- Bootstrap and custom CSS for styling
- JavaScript for interactivity and MQTT communication

When you click a button:
1. The browser publishes an "ON" or "OFF" message to the topic `/charles/light_control`
2. The interface updates to show the current state

### Simulated IoT Device (light_simulation.py)

The Python script:
1. Connects to the same HiveMQ broker using the paho-mqtt library
2. Subscribes to the `/charles/light_control` topic
3. Prints messages when it receives "ON" or "OFF" commands

## Troubleshooting

### Connection Issues

If you see "Authorization failed" or connection errors:

1. **Check Internet Connection**:
   - Ensure you have a stable internet connection

2. **Firewall Settings**:
   - Make sure your firewall allows WebSocket connections on port 8884

3. **Browser Console**:
   - Open your browser's developer console (F12) to see detailed error messages

### Python Script Issues

If the Python script fails to connect:

1. **Check Dependencies**:
   - Ensure paho-mqtt is installed: `pip install paho-mqtt`

2. **TLS/SSL Issues**:
   - Make sure your Python environment supports TLS connections

## Customization

### Changing MQTT Broker

To use your own MQTT broker:

1. Edit `light_simulation.py`:
   - Update the `BROKER`, `PORT`, `USERNAME`, and `PASSWORD` constants

2. Edit `index.html`:
   - Find the MQTT connection section and update the connection URL and credentials

### Changing the Topic

To use a different topic:

1. Edit `light_simulation.py`:
   - Update the `TOPIC` constant

2. Edit `index.html`:
   - Update the `topic` variable
   - Update the topic check in the message handler

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- HiveMQ for providing a free MQTT broker
- MQTT.js for the browser-based MQTT client
- Paho for the Python MQTT client
