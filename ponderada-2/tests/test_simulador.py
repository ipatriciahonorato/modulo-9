import unittest
from paho.mqtt import client as mqtt_client
import time
import threading

# Configuration
broker = 'localhost'
port = 1891
topic = "sps30/topic"
client_id_publisher = 'python_publisher_test'
client_id_subscriber = 'python_subscriber_test'

# Global variable to store received messages for validation
received_messages = []

def setup_subscriber():
    def on_message(client, userdata, message):
        received_messages.append(message.payload.decode())
        print(f"Received message in test subscriber: {message.payload.decode()}")

    subscriber = mqtt_client.Client(client_id_subscriber)
    subscriber.on_message = on_message
    subscriber.connect(broker, port)
    subscriber.subscribe(topic)
    subscriber.loop_start()
    return subscriber

class TestIoTSimulator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subscriber = setup_subscriber()
        time.sleep(1)  # Ensure subscriber setup before tests run

    @classmethod
    def tearDownClass(cls):
        cls.subscriber.loop_stop()
        cls.subscriber.disconnect()

    def test_data_reception(self):
        """Test if data is received by the broker."""
        publisher = mqtt_client.Client(client_id_publisher)
        publisher.connect(broker, port)
        test_message = "Test message"
        publisher.publish(topic, test_message)
        time.sleep(2)  # Wait for message to be received

        self.assertIn(test_message, received_messages, "The test message was not received.")

    def test_data_validation(self):
        """Test if received data matches sent data."""
        # Assuming test_data_reception already adds a message to received_messages
        self.assertEqual(received_messages[-1], "Test message", "The received message does not match the sent message.")

    def test_message_dispatch_rate(self):
        """Test if messages are dispatched at the expected rate."""
        publisher = mqtt_client.Client(client_id_publisher)
        publisher.connect(broker, port)
        start_time = time.time()
        for _ in range(2):
            publisher.publish(topic, "Rate test message")
            time.sleep(5)  # Dispatch rate of 5 seconds

        end_time = time.time()
        duration = end_time - start_time

        # Expecting 2 messages, with a 5-second gap, allowing 1 second as margin
        expected_duration_min = 9  # seconds
        expected_duration_max = 11  # seconds
        self.assertTrue(expected_duration_min <= duration <= expected_duration_max, "The dispatch rate does not match the expected rate.")

if __name__ == '__main__':
    unittest.main()
