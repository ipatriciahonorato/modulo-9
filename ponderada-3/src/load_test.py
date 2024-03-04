import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

client.connect("localhost", 1883, 60)

for i in range(1000):
    client.publish("generic/topic", f"Message {i}")
    time.sleep(0.01)

client.disconnect()

