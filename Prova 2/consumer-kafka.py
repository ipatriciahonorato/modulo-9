from confluent_kafka import Consumer, KafkaError
import json

consumer_config = {
    'bootstrap.servers': 'localhost:29092,localhost:39092',
    'group.id': 'air-quality-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(**consumer_config)
consumer.subscribe(['qualidadeAr'])

#Função que salva os dados no arquivo para mostrar a persistência de dados

def save_data_to_file(data, filename="sensor_data.txt"):
    with open(filename, "a") as file:
        file.write(f"{data}\n")

# Função que formata os dados gerado pelo producer para serem exibidos no terminal
def format_sensor_data(data):
    return (
        f"Sensor ID    : {data['idSensor']}\n"
        f"Timestamp    : {data['timestamp']}\n"
        f"Pollutant    : {data['tipoPoluente']}\n"
        f"Level        : {data['nivel']}\n"
        "------------------------------------\n"
    )

try:
    print("Listening for messages on 'qualidadeAr' topic...")
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() != KafkaError._PARTITION_EOF:
                print(f"Consumer error: {msg.error()}")
            continue
        
        sensor_data = json.loads(msg.value().decode('utf-8'))
        formatted_data = format_sensor_data(sensor_data)
        print(formatted_data)  # Exibe os dados formatados no terminal
        save_data_to_file(formatted_data)  # Salva os dados em um arquivo
except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    consumer.close()


