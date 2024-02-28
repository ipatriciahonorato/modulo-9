# Simulador de dispositivos IoT

## 1. Objetivo
Criar um simulador de dispositivos IoT utilizando o protocolo MQTT através do uso da biblioteca Eclipse Paho.

## 2. Enunciado
A primeira atividade do módulo tem como objetivo a criação de um simulador de dispositivos IoT capaz de enviar informações em um tópico com o formato de dados consistente com os seguintes dispositivos de exemplo:

- Sensor de Radiação Solar

- SPS30

- MiCS-6814

Escolha ao menos um desses sensores e estude o seu datasheed para reproduzir o que seria uma mensagem MQTT gerada a partir dos dados aferidos por eles. Foque na reprodução fidedigna de taxa de comunicação, unidade e ordem de grandeza das medições. Utilize alguma técnica/biblioteca para que suas mensagens simuladas não sejam todas iguais (mas todas dentro das especificações do componente).

Embora não haja o requerimento de criar testes automatizados, o simulador deve apresentar evidências objetivas de funcionamento.

# Descrição do Projeto

Este projeto visa criar um simulador de dispositivos IoT que utiliza o protocolo MQTT para enviar mensagens simuladas, replicando os dados que seriam gerados por dispositivos reais. Foi escolhido o sensor SPS30 para simulação, focando na reprodução fidedigna de sua taxa de comunicação, unidade e ordem de grandeza das medições. O objetivo é fornecer uma ferramenta para testar e desenvolver aplicações IoT sem a necessidade de hardware real.

## Tecnologias

- **Linguagem de Programação:** Python
- **Biblioteca MQTT:** Eclipse Paho MQTT Python Client
- **Simulação de Dados:** Random para geração de dados simulados

## Instalação e Configuração

### Clonar o Repositório
        git clone <https://github.com/ipatriciahonorato/modulo-9.git>
	    cd <ponderada-1>
### Instalar Dependências
Antes de rodar o simulador, é necessário instalar a biblioteca Eclipse Paho MQTT Python.

    pip install paho-mqtt

### Configuração do Broker MQTT
O simulador requer um broker MQTT rodando localmente ou em um servidor acessível. Este projeto foi testado com Mosquitto, um broker MQTT leve. A configuração do broker não está inclusa neste guia, mas você pode encontrar instruções detalhadas em [mosquitto.org](https://mosquitto.org/)

## Principais Funcionalidades com Código
Este projeto inclui duas funcionalidades principais: a simulação de dados do sensor SPS30 e a comunicação desses dados via protocolo MQTT. Abaixo estão detalhadas as implementações dessas funcionalidades:

1. **Simulação de Dados do Sensor SPS30:** O arquivo `publisher.py` contém a lógica para gerar dados simulados que imitam as leituras de um sensor SPS30 real. Utiliza a biblioteca `random` para gerar valores dentro de um intervalo específico, representando as concentrações de massa (µg/m³) e número (#/cm³) de partículas.

    `import random`
    
    `def generate_sps30_data():
        # Geração de valores simulados para concentrações de massa
        pm1 = random.uniform(0, 50)  # PM1.0
        pm2_5 = random.uniform(5, 75)  # PM2.5
        pm4 = random.uniform(5, 100)  # PM4.0
        pm10 = random.uniform(10, 120)  # PM10`
    
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

2. **Publicação de Mensagens MQTT:** Após a geração dos dados simulados, o `publisher.py` publica essas informações em um tópico MQTT. Isso é feito utilizando a biblioteca Eclipse Paho MQTT. A publicação é contínua, com um intervalo de 5 segundos entre cada mensagem.

`import paho.mqtt.client as mqtt
    import time`
    
    #Configuração do cliente e conexão ao broker MQTT
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_publisher")
    client.connect("localhost", 1891)  
    
    try:
        while True:
            message = generate_sps30_data()
            client.publish("sps30/topic", message)
            print(f"Publicado: {message}")
            time.sleep(5)  # Intervalo de 5 segundos entre publicações
    except KeyboardInterrupt:
        print("Publicação encerrada pelo usuário")
        client.disconnect()`
   
3. **Subscrição e Recebimento de Mensagens MQTT:** O arquivo `subscriber.py` é responsável por se inscrever no tópico onde os dados do sensor SPS30 são publicados e por exibir as mensagens recebidas, facilitando a verificação do fluxo de dados.

`import paho.mqtt.client as mqtt`

    def on_message(client, userdata, message):
        print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")
    
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect("localhost", 1891, 60)
    client.loop_forever()
   
Estas funcionalidades formam a base do simulador de dispositivos IoT, permitindo a simulação de dados de um sensor SPS30 e a comunicação desses dados através do protocolo MQTT, demonstrando a aplicabilidade do projeto em ambientes de teste e desenvolvimento

## Execução do Simulador de Dispositivos IoT

### Iniciando o Broker MQTT
- **Mosquitto:** Certifique-se de que o Mosquitto esteja instalado em seu sistema. Para iniciar o Mosquitto com o arquivo de configuração personalizado, use o comando:

`/meu_workspace/modulo-9/ponderada-1/conf_mosquitto`

`mosquitto -c mosquitto.conf`

### Executando o Simulador
- **Publicador (publisher.py)**: Este script gera e publica dados simulados do sensor SPS30 em um tópico MQTT específico. Para executá-lo, navegue até o diretório do projeto e use o comando:

`python3 publisher.py
`
- **Subscritor (subscriber.py):** Este script se inscreve no tópico sps30/topic e exibe as mensagens recebidas. Para iniciar o subscritor, abra um novo terminal, navegue até o diretório do projeto e execute:


`python3 subscriber.py
`
### Verificação de Funcionamento
- **Publicador:** Verifique o terminal onde o publisher.py está sendo executado para garantir que as mensagens estejam sendo publicadas regularmente.
- **Subscritor:** No terminal do subscriber.py, confirme que as mensagens estão sendo recebidas e exibidas corretamente.

## Demonstração do projeto

[![O vídeo a seguir apresenta o simulador desenvolvido para esse projeto](https://i3.ytimg.com/vi/Z0yaUPNVQaA/maxresdefault.jpg)](https://youtu.be/Z0yaUPNVQaA)

## Referências
Datasheet do Sensor SPS30: [SPS30 Datasheet](https://www.alldatasheet.com/view.jsp?Searchword=Sps30%20datasheet&gad_source=1&gclid=CjwKCAiA7t6sBhAiEiwAsaieYhkbnMeIYLDdvsNp4culvHNBwikKTM4QvT16S8ImRQTC9o1Dl6LQ-BoCe8cQAvD_BwE)



