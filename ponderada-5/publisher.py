import paho.mqtt.client as mqtt
import time
import random
import ssl
import os
import json  # Importar json para trabalhar com dados no formato JSON

# Carrega configurações de variáveis de ambiente
broker = os.getenv("MQTT_BROKER")
port = int(os.getenv("MQTT_PORT"))
username = os.getenv("MQTT_USERNAME")
password = os.getenv("MQTT_PASSWORD")

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

# Configurações de TLS e autenticação
client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)

# Conexão ao broker HiveMQ
client.connect(broker, port, 60)

def generate_sps30_data():
    # Geração de valores simulados para concentrações de massa e número (dicionário)
    data = {
        'PM1': random.uniform(0, 50),  # PM1.0
        'PM2_5': random.uniform(5, 75),  # PM2.5
        'PM4': random.uniform(5, 100),  # PM4.0
        'PM10': random.uniform(10, 120),  # PM10
        'PM0_5_num': random.uniform(0, 1000),  # PM0.5
        'PM1_num': random.uniform(100, 5000),  # PM1.0
        'PM2_5_num': random.uniform(200, 7000),  # PM2.5
        'PM4_num': random.uniform(300, 10000),  # PM4.0
        'PM10_num': random.uniform(400, 15000)  # PM10
    }

    # Conversão dos dados para uma string JSON
    message = json.dumps(data)
    return message

try:
    while True:
        message = generate_sps30_data()
        client.publish("sps30/topic", message)
        print(f"Publicado: {message}")
        time.sleep(5)  # Intervalo de 5 segundos entre publicações

except KeyboardInterrupt:
    print("Publicação encerrada pelo usuário")
    client.disconnect()
