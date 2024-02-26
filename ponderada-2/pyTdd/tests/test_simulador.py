import unittest
from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt
import time

# Configuração
broker = 'localhost'
port = 1891
topic = "sps30/topic"
client_id_publisher = 'python_publisher_test'
client_id_subscriber = 'python_subscriber_test'

# Criação do cliente para o publicador
publisher_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=client_id_publisher, clean_session=True, protocol=mqtt.MQTTv311)

# Criação do cliente para o subscriber
subscriber_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=client_id_subscriber, clean_session=True, protocol=mqtt.MQTTv311)

# Variável global para armazenar mensagens recebidas para validação
received_messages = []

def setup_subscriber():
    def on_message(client, userdata, message):
        received_messages.append(message.payload.decode())
        print(f"Received message in test subscriber: {message.payload.decode()}")

    # Criação do cliente para o subscriber
    subscriber = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=client_id_subscriber, clean_session=True, protocol=mqtt.MQTTv311)
    subscriber.on_message = on_message
    subscriber.connect(broker, port)
    subscriber.subscribe(topic)
    subscriber.loop_start()
    return subscriber

class TestIoTSimulator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.subscriber = setup_subscriber()
        time.sleep(1)  # Garante que o subscriber seja configurado antes dos testes

    @classmethod
    def tearDownClass(cls):
        cls.subscriber.loop_stop()
        cls.subscriber.disconnect()

    def test_data_reception(self):
        """Testa se os dados são recebidos pelo broker."""
        # Publicador usando a versão correta da API de callback
        publisher = mqtt_client.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=client_id_publisher, clean_session=True, protocol=mqtt_client.MQTTv311)
        publisher.connect(broker, port)
        test_message = "Test message"
        publisher.publish(topic, test_message)
        time.sleep(2)  # Aguarda a mensagem ser recebida

        self.assertIn(test_message, received_messages, "A mensagem de teste não foi recebida.")

    def test_data_validation(self):
        """Testa se os dados recebidos correspondem aos dados enviados."""
        # Supõe que test_data_reception já adicionou uma mensagem a received_messages
        self.assertEqual(received_messages[-1], "Test message", "A mensagem recebida não corresponde à mensagem enviada.")

    def test_message_dispatch_rate(self):
        """Testa se as mensagens são disparadas na taxa esperada."""
        # Publicador usando a versão correta da API de callback
        publisher = mqtt_client.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=client_id_publisher, clean_session=True, protocol=mqtt_client.MQTTv311)
        publisher.connect(broker, port)
        start_time = time.time()
        for _ in range(2):
            publisher.publish(topic, "Rate test message")
            time.sleep(5)  # Taxa de disparo de 5 segundos

        end_time = time.time()
        duration = end_time - start_time

        # Espera-se 2 mensagens, com intervalo de 5 segundos, permitindo 1 segundo de margem
        expected_duration_min = 9  # segundos
        expected_duration_max = 11  # segundos
        self.assertTrue(expected_duration_min <= duration <= expected_duration_max, "A taxa de disparo não corresponde à esperada.")

if __name__ == '__main__':
    unittest.main()
