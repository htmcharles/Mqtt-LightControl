import paho.mqtt.client as mqtt

# MQTT Connection Constants
BROKER = "54d38e6010684c31a4d8ac17a897978b.s1.eu.hivemq.cloud"
PORT = 8884
TOPIC = "/charles/light_control"
USERNAME = "charles"
PASSWORD = "Charles1"

# Callback when a message is received
def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    if msg == "ON":
        print("💡 Light is TURNED ON")
    elif msg == "OFF":
        print("💡 Light is TURNED OFF")

# Create an MQTT client instance
client = mqtt.Client()

# Set TLS for secure connection
client.tls_set()

# Set username and password
client.username_pw_set(USERNAME, PASSWORD)

# Assign the callback for receiving messages
client.on_message = on_message

# Connect to the broker and subscribe to the topic
print(f"Connecting to broker {BROKER} on port {PORT}...")
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

# Loop forever to keep the script running and listening for messages
print(f"Waiting for messages on topic {TOPIC}...")
client.loop_forever()
