# MQTT Light Control Project

This project implements a web-based light control system using MQTT protocol. It consists of a web interface to control a light and a Python script that simulates an ESP8266 IoT device.

## Components

1. **Web Interface (index.html)**
   - A modern, responsive web interface with ON/OFF controls
   - Real-time status updates
   - Dark mode support
   - MQTT communication via WebSocket

2. **IoT Device Simulation (light_simulation.py)**
   - Python script simulating an ESP8266 device
   - Subscribes to MQTT messages
   - Prints light status changes

## Setup Instructions

1. Install required Python packages:
   ```bash
   pip install paho-mqtt
   ```

2. Run the Python simulation script:
   ```bash
   python light_simulation.py
   ```

3. Open `index.html` in a web browser

## Testing

1. The Python script will connect to the MQTT broker and wait for messages
2. Open the web interface in your browser
3. Click the ON/OFF buttons to control the light
4. Observe the status changes in both the web interface and Python console

## MQTT Details

- Broker: broker.hivemq.com
- Port: 1883 (Python), 8000 (WebSocket)
- Topic: /student_group/light_control
- Messages: "ON" or "OFF"

## Technologies Used

- HTML5
- CSS3
- JavaScript
- MQTT.js
- Python
- paho-mqtt

## Features

- **Real-time Control**: Control the light in real-time using MQTT messages.
- **User-Friendly Interface**: A web-based interface for easy interaction.
- **Dark Mode**: Toggle between light and dark themes for better visibility.
- **Connection Status**: Visual indicators for connection status to the MQTT broker.

## How to Run

### Prerequisites

- Python 3.x installed on your machine.
- Internet connection for accessing the public MQTT broker.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sm-junior0/Mqtt-LightControl.git
   ```

2. **Install Dependencies**:
   Make sure to install the required Python library:
   ```bash
   pip install paho-mqtt
   ```

3. **Run the Simulation**:
   Execute the `light_simulation.py` script to simulate the IoT device:
   ```bash
   python light_simulation.py
   ```

4. **Open the Web Interface**:
   Open `index.html` in your web browser to control the light.

## MQTT Broker

The application connects to a public MQTT broker at `ws://broker.hivemq.com:8000/mqtt`. You can change the broker URL in the JavaScript code if you want to use a different broker.

## Dependencies

- **Python Libraries**:
  - `paho-mqtt`: A Python library for MQTT.

- **Web Technologies**:
  - HTML
  - CSS
  - JavaScript
  - MQTT.js (for MQTT protocol)
  - Bootstrap (for styling)
  - Font Awesome (for icons)

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to report issues, please feel free to submit a pull request or open an issue.

## Acknowledgments

- [MQTT.js](https://github.com/mqttjs/MQTT.js) for the MQTT client implementation.
- [Bootstrap](https://getbootstrap.com/) for responsive design.
- [Font Awesome](https://fontawesome.com/) for icons.
- [Paho MQTT](https://www.eclipse.org/paho/) for the Python MQTT client library.

---

This version of the README retains the original structure and content while ensuring clarity and simplicity. No additional features or complexities have been added. Let me know if you need further adjustments!
