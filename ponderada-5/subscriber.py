import os
import json
import paho.mqtt.client as mqtt
import ssl
from pymongo import MongoClient

# Acessa as configurações a partir das variáveis de ambiente
broker = os.getenv("MQTT_BROKER")
port = int(os.getenv("MQTT_PORT"))
username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")
topic = os.getenv("MQTT_TOPIC")

# Conectar ao MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['meu_banco_de_dados']  # Altere para o nome do seu banco de dados
colecao = db['minha_colecao']  # Altere para o nome da sua coleção

def on_message(client, userdata, message):
    """Callback quando uma mensagem é recebida."""
    data = message.payload.decode()
    print(f"Recebido: {data} no tópico {message.topic}")
    data_dict = json.loads(data)  # Certifique-se de que a mensagem é um JSON válido
    resultado_insercao = colecao.insert_one(data_dict)
    print(f'Documento inserido com o ID: {resultado_insercao.inserted_id}')

def on_connect(client, userdata, flags, rc, properties=None):
    """Função que conecta ao broker."""
    if rc == 0:
        print("Conectado ao broker")
        client.subscribe(topic)
    else:
        print(f"Falha na conexão, código de retorno {rc}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS_CLIENT)
client.username_pw_set(username, password)

client.connect(broker, port, 60)

client.loop_forever()
