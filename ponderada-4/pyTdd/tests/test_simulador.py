import unittest
from paho.mqtt import client as mqtt_client
import time
import ssl
import configparser

# Lendo as configurações do arquivo
config = configparser.ConfigParser()
config.read('config.ini')

# Configuração para conexão com o HiveMQ utilizando as informações do arquivo
broker = config.get('mqtt', 'broker')
port = config.getint('mqtt', 'port')
topic = config.get('mqtt', 'topic')
client_id_publisher = config.get('mqtt', 'client_id_publisher')
client_id_subscriber = config.get('mqtt', 'client_id_subscriber')
username = config.get('mqtt', 'username')
password = config.get('mqtt', 'password')


def tls_set(client):
    """Configura a conexão TLS."""
    client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS)
    client.username_pw_set(username, password)


def setup_subscriber():
    """Prepara e inicia o subscriber."""
    received_messages = []

    def on_message(client, userdata, message):
        received_message = message.payload.decode()
        print(f"Received message in test subscriber: {received_message}")
        received_messages.append(received_message)

    subscriber = mqtt_client.Client(
        callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2,
        client_id=client_id_subscriber, clean_session=True,
        protocol=mqtt_client.MQTTv311)
    tls_set(subscriber)
    subscriber.on_message = on_message
    subscriber.connect(broker, port)
    subscriber.subscribe(topic)
    subscriber.loop_start()
    return subscriber, received_messages


class TestIoTSimulator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configura o ambiente de teste antes da execução dos testes."""
        cls.subscriber, cls.received_messages = setup_subscriber()
        time.sleep(1)  # Espera para garantir a configuração do subscriber

    @classmethod
    def tearDownClass(cls):
        """Limpa o ambiente de teste após a execução dos testes."""
        cls.subscriber.loop_stop()
        cls.subscriber.disconnect()

    def test_data_reception(self):
        """Verifica se os dados são recebidos pelo broker."""
        # Configura e conecta o publisher
        publisher = mqtt_client.Client(
            callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2,
            client_id=client_id_publisher, clean_session=True,
            protocol=mqtt_client.MQTTv311)
        tls_set(publisher)  # Aplica configuração TLS
        publisher.connect(broker, port)
        test_message = "Test message"
        publisher.publish(topic, test_message)
        time.sleep(2)  # Aguarda a recepção da mensagem

        # Testa se a mensagem foi recebida
        self.assertIn(test_message, self.received_messages,
                      "A mensagem de teste não foi recebida.")

    def test_data_validation(self):
        """Confirma se os dados recebidos correspondem aos dados enviados."""
        self.assertEqual(self.received_messages[-1], "Test message",
                         "A mensagem recebida não corresponde à enviada.")

    def test_message_dispatch_rate(self):
        """Verifica se as mensagens são enviadas na taxa esperada."""
        # Configura e conecta o publisher
        publisher = mqtt_client.Client(
            callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2,
            client_id=client_id_publisher, clean_session=True,
            protocol=mqtt_client.MQTTv311)
        tls_set(publisher)  # Aplica configuração TLS
        publisher.connect(broker, port)
        start_time = time.time()
        # Envia duas mensagens com intervalo de 5 segundos
        for _ in range(2):
            publisher.publish(topic, "Rate test message")
            time.sleep(5)

        end_time = time.time()
        duration = end_time - start_time

        # Verifica se o intervalo de envio está dentro do esperado
        expected_duration_min = 9  # segundos
        expected_duration_max = 11  # segundos
        self.assertTrue(
            expected_duration_min <= duration <= expected_duration_max,
            "A taxa de disparo não corresponde à esperada."
        )


if __name__ == '__main__':
    unittest.main()
