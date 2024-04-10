# Importação de Bibliotecas
import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

# Configuração do cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")

# Conexão ao broker MQTT
client.connect("localhost", 1891)


def generate_humidity_data():
    # Escolhe aleatoriamente entre hortaliças e flores
    sensor_type = random.choice(["hortaliças", "flores"])
    # Geração de valor de umidade simulado
    if sensor_type == "hortaliças":
        humidity = random.uniform(20, 80)
    else:
        humidity = random.uniform(30, 90)
    # ID do dispositivo e timestamp da medição
    device_id = f"gh{random.randint(1,3)}h{random.randint(1,5)}"
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

    # Criação da mensagem com os dados simulados
    message = {
        "id": device_id,
        "tipo": sensor_type,
        "umidade": round(humidity, 2),
        "timestamp": timestamp
    }
    return message


# Publicação de mensagens MQTT
try:
    while True:
        data = generate_humidity_data()
        topic = f"estufa/{data['id']}/{data['tipo']}"
        client.publish(topic, str(data))
        print(f"Publicado em {topic}: {data}")
        time.sleep(5)  # Intervalo de 5 segundos entre publicações

except KeyboardInterrupt:
    print("Publicação encerrada pelo usuário")
    client.disconnect()
