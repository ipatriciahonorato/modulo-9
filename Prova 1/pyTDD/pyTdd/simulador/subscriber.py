# Importação de Bibliotecas

import paho.mqtt.client as mqtt


# Callback quando uma mensagem é recebida
def on_message(client, userdata, message):
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")


# Função que conecta ao broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Conectado ao broker")
        client.subscribe("sps30/topic")
    else:
        print(f"Falha na conexão, código de retorno {rc}")


# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()
