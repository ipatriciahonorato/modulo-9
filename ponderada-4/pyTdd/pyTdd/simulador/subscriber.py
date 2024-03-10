import os
import paho.mqtt.client as mqtt
import ssl

# Acessa as configurações a partir das variáveis de ambiente
broker = os.getenv("MQTT_BROKER")
port = int(os.getenv("MQTT_PORT"))
username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")
topic = os.getenv("MQTT_TOPIC")


def on_message(client, userdata, message):
    """Callback quando uma mensagem é recebida."""
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")


def on_connect(client, userdata, flags, rc, properties=None):
    """Função que conecta ao broker."""
    if rc == 0:
        print("Conectado ao broker")
        client.subscribe(topic)
    else:
        print(f"Falha na conexão, código de retorno {rc}")


# Configuração do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Configurações de TLS e autenticação
client.tls_set(cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_TLS_CLIENT)
client.username_pw_set(username, password)

# Conecta ao broker HiveMQ
client.connect(broker, port, 60)

# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()
