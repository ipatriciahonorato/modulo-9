import paho.mqtt.client as mqtt
import time
import random
import ssl
import os

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
    # Geração de valores simulados para concentrações de massa
    pm1 = random.uniform(0, 50)  # PM1.0
    pm2_5 = random.uniform(5, 75)  # PM2.5
    pm4 = random.uniform(5, 100)  # PM4.0
    pm10 = random.uniform(10, 120)  # PM10

    # Geração de valores simulados para concentrações de número
    pm0_5_num = random.uniform(0, 1000)  # PM0.5
    pm1_num = random.uniform(100, 5000)  # PM1.0
    pm2_5_num = random.uniform(200, 7000)  # PM2.5
    pm4_num = random.uniform(300, 10000)  # PM4.0
    pm10_num = random.uniform(400, 15000)  # PM10

    # Criação da mensagem com os dados simulados
    message = (f"SPS30 PM1.0: {pm1:.2f} µg/m³, PM2.5: {pm2_5:.2f} µg/m³, "
               f"PM4.0: {pm4:.2f} µg/m³, PM10: {pm10:.2f} µg/m³, "
               f"PM0.5#: {pm0_5_num:.0f} #/cm³, PM1.0#: {pm1_num:.0f} #/cm³, "
               f"PM2.5#: {pm2_5_num:.0f} #/cm³, PM4.0#: {pm4_num:.0f} #/cm³, "
               f"PM10#: {pm10_num:.0f} #/cm³")

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
