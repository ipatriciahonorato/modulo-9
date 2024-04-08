from confluent_kafka import Consumer, KafkaError

# Configurações do Consumer Kafka
conf = {
    'bootstrap.servers': 'pkc-7xoy1.eu-central-1.aws.confluent.cloud:9092',  # Substitua pelo seu endpoint do Kafka
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': '[placeholder]',  # Substitua pelo seu Kafka API Key
    'sasl.password': '[placeholder]',  # Substitua pela sua Kafka API Secret
    'group.id': 'mqtt_kafka_group',  # ID do Grupo de Consumo
    'auto.offset.reset': 'earliest'
}

# Criação do Consumer com a configuração fornecida
consumer = Consumer(conf)
consumer.subscribe(['sensor'])  # Subscrevendo ao tópico 'sensor'

try:
    while True:
        # Polling de mensagens do Kafka
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # Fim da partição alcançado
                continue
            else:
                print(msg.error())
                break

        # Mensagem recebida
        print(f'Recebido: {msg.value().decode("utf-8")}')

except KeyboardInterrupt:
    print('Interrompido pelo usuário')

finally:
    # Fechamento do Consumer
    consumer.close()
