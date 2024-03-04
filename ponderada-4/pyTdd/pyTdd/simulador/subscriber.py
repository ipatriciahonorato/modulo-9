import paho.mqtt.client as mqtt
import ssl
import configparser

# Lê as configurações do arquivo
config = configparser.ConfigParser()
config.read('config.ini')

# Acessa as configurações do arquivo config.ini
broker = config['mqtt']['broker']
port = int(config['mqtt']['port'])
username = config['mqtt']['username']
password = config['mqtt']['password']
topic = config['mqtt']['topic']


# Callback quando uma mensagem é recebida
def on_message(client, userdata, message):
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")


# Função que conecta ao broker
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Conectado ao broker")
        client.subscribe(topic)
    else:
        print(f"Falha na conexão, código de retorno {rc}")


# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Configurações de TLS e autenticação
client.tls_set(cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)

# Conecte ao broker HiveMQ
client.connect(broker, port, 60)
# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()
