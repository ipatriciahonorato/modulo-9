from confluent_kafka import Producer
import json
import time
from random import randint, uniform

producer_config = {
    'bootstrap.servers': 'localhost:29092,localhost:39092',
    'client.id': 'air-quality-producer'
}

producer = Producer(**producer_config)

#Função para gerar dados do sensor no formato especificado

def generate_sensor_data(sensor_id):
    return {
        "idSensor": sensor_id,
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "tipoPoluente": "PM2.5",
        "nivel": round(uniform(10, 50), 2)  # Simula um valor entre 10 e 50
    }

def produce_air_quality_data():
    sensor_id = f"sensor_{randint(1, 100):03d}"  # Gera um ID de sensor aleatório
    data = generate_sensor_data(sensor_id)
    
    def delivery_callback(err, msg):
        if err:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    payload = json.dumps(data)
    producer.produce("qualidadeAr", payload.encode('utf-8'), callback=delivery_callback)
    producer.flush()

# Simula o envio de dados a cada 5 segundos
while True:
    produce_air_quality_data()
    time.sleep(5)  # Intervalo de envio

