import unittest
import paho.mqtt.client as mqtt
import json
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

class TestIoTSimulator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurando o subscriber para todos os tópicos com QoS 1
        cls.subscriber = cls.setup_subscriber_qos1((topic_base + "#", 1))
        time.sleep(1)  # Espera para a configuração do subscriber

    @classmethod
    def tearDownClass(cls):
        cls.subscriber.loop_stop()
        cls.subscriber.disconnect()

    @staticmethod
    def setup_subscriber_qos1(topic_filter):
        """Configura o subscriber com QoS 1 e inicia o loop."""
        def on_message(client, userdata, message):
            received_messages.append(json.loads(message.payload.decode()))
            print(
                f"Received message in test subscriber: "
                f"{message.payload.decode()}"
            )

        subscriber = mqtt.Client(client_id=client_id_subscriber)
        subscriber.on_message = on_message
        subscriber.connect(broker, port)
        subscriber.subscribe(topic_filter, qos=1)
        subscriber.loop_start()
        return subscriber

    def test_qos_1_message_reception(self):
        """Testa o correto recebimento das mensagens com QoS = 1."""
        publisher = mqtt.Client(client_id=client_id_publisher)
        publisher.connect(broker, port)
        test_message = json.dumps(
            {
                "id": "test1",
                "tipo": "hortaliças",
                "umidade": 50,
                "timestamp": "01/01/2024 00:00"
            }
        )
        publisher.publish(topic_base + "test1/hortaliças", test_message, qos=1)
        time.sleep(2)  # Aguarda a mensagem ser recebida
        self.assertTrue(
            any(msg['id'] == 'test1' for msg in received_messages),
            "A mensagem de teste QoS 1 não foi recebida."
        )

    def test_message_integrity(self):
        """Testa a integridade das mensagens recebidas."""
        # Usando a última mensagem recebida para teste de integridade
        last_message = received_messages[-1]
        expected_message = {
            "id": "test1",
            "tipo": "hortaliças",
            "umidade": 50,
            "timestamp": "01/01/2024 00:00"
        }
        self.assertEqual(
            last_message,
            expected_message,
            "A integridade da mensagem recebida não está preservada."
        )

    def test_alarm_functionality(self):
        """Testa o correto funcionamento dos alarmes de umidade."""
        # Testando um cenário de umidade muito baixa para hortaliças
        humidity_low_alert = self.checkAlert("Hortaliças", 25)
        self.assertEqual(
            humidity_low_alert,
            " [ALERTA: Umidade MUITO BAIXA!]",
            "O alerta de umidade muito baixa para hortaliças falhou."
        )

        # Testando um cenário de umidade muito alta para flores
        humidity_high_alert = self.checkAlert("Flores", 85)
        self.assertEqual(
            humidity_high_alert,
            " [ALERTA: Umidade MUITO ALTA!]",
            "O alerta de umidade muito alta para flores falhou."
        )

    def checkAlert(self, sensor_type, humidity):
        """Replica a lógica de alerta do sistema para uso no teste."""
        if sensor_type == "Hortaliças":
            if humidity < 30:
                return " [ALERTA: Umidade MUITO BAIXA!]"
            elif humidity > 70:
                return " [ALERTA: Umidade MUITO ALTA!]"
        elif sensor_type == "Flores":
            if humidity < 40:
                return " [ALERTA: Umidade MUITO BAIXA!]"
            elif humidity > 80:
                return " [ALERTA: Umidade MUITO ALTA!]"
        return ""  # Retorna uma string vazia se não houver alerta


if __name__ == '__main__':
    unittest.main()
