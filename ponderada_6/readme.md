# Integração entre HiveMQ e Kafka Cloud

## 1. Enunciado

Nessa atividade, deve-se desenvonver a integração entre o cluster do HiveMQ e um provedor de Kafka em nuvem.

## Descrição do Projeto

Este projeto visa a integração entre um cluster MQTT (HiveMQ) e um provedor de Kafka em nuvem (Confluent Cloud), permitindo a transmissão de mensagens de sensores ambientais de um publisher MQTT para um consumer Kafka. Essa integração é fundamental para cenários de IoT (Internet das Coisas), onde dispositivos dispersos publicam dados em tempo real que são consumidos e processados por sistemas em nuvem.

## Tecnologias

- MQTT: Protocolo leve de mensageria usado para comunicação entre dispositivos IoT.
- HiveMQ: Broker MQTT que facilita a comunicação entre dispositivos IoT e aplicações backend.
- Kafka: Plataforma de streaming de eventos que permite a manipulação de streams de dados em tempo real.
- Confluent Cloud: Serviço em nuvem que oferece instâncias gerenciadas do Kafka.
- Python: Linguagem de programação usada para escrever os scripts de publisher e subscriber.

## Componentes do Projeto

### Publisher MQTT

Este script atua como um publisher MQTT, simulando dados de sensores de partículas no ar, como PM1.0, PM2.5, PM4.0, e PM10, tanto em termos de concentração de massa quanto de número de partículas. Utiliza a biblioteca paho.mqtt para estabelecer uma conexão segura com um broker MQTT (HiveMQ), autenticando-se com credenciais armazenadas em variáveis de ambiente. Uma vez conectado, ele publica, em um intervalo de 5 segundos, dados gerados aleatoriamente para um tópico MQTT especificado, até que o processo seja interrompido manualmente.


### Subscriber Kafka (Consumer)

O script subscriber.py é configurado para funcionar como um consumer Kafka, conectando-se ao cluster Kafka na Confluent Cloud. Ele consome mensagens de um tópico Kafka especificado ("sensor"), que são originadas do broker MQTT e encaminhadas via um conector MQTT Source configurado no Kafka Connect. O script utiliza a biblioteca confluent_kafka para autenticar no cluster Kafka usando SASL/SSL com uma API Key e Secret, e entra em um loop onde mensagens são continuamente consumidas e impressas no console. Esse processo também continuará até ser interrompido manualmente.

## Instalação e Configuração do Projeto

### Clonagem do repositório

```
git clone https://github.com/ipatriciahonorato/modulo-9.git
cd modulo-9/ponderada_6
```

### Kafka e HiveMQ

**1. HiveMQ Cloud:**

- Acesse HiveMQ Cloud e crie uma conta ou faça login.
- Crie um novo cluster MQTT seguindo as instruções na plataforma.
- Anote as credenciais (URI, porta, usuário e senha) para uso no Publisher.


**2. Confluent Cloud:**

- Acesse Confluent Cloud e crie uma conta ou faça login.
- Siga o guia de início rápido para configurar um novo cluster Kafka.
- Crie um tópico Kafka (ex: "sensor").
- Gere uma API Key e Secret para autenticação e anote-os para uso no Subscriber e no Conector MQTT Source.

**3. Conector MQTT Source:**

- Na interface da Confluent Cloud, acesse a seção "Connectors" e configure um novo MQTT Source Connector.
- Utilize as credenciais do HiveMQ e da Confluent Cloud conforme descrito anteriormente para conectar o HiveMQ ao tópico Kafka.

## Execução do Projeto

### Execute o Publisher MQTT:

No terminal, na pasta do arquivo, execute:

```
python3 publisher.py
```
Isso irá começar a publicar dados simulados de sensores no broker MQTT.

### Execute o Subscriber Kafka (Consumer):

Abra um novo terminal, navegue até a pasta do subscriber e execute:
```
python subscriber.py
```
O subscriber irá consumir as mensagens do tópico Kafka configurado e exibir os dados recebidos.

## Visualização do Projeto

As mensagens enviadas pelo publisher **serão exibidas no terminal do subscriber e também na aba de mensagens tópico no Confluent Cloud**, indicando que a integração entre o HiveMQ e o Kafka está funcionando corretamente. As mensagens exibirão dados simulados dos sensores ambientais.

## Procedimentos de Testes

### Verifique o funcionamento do Consumer Kafka:

Assegure-se de que o script subscriber.py esteja executando e aguardando por mensagens.


### Verifique o funcionamento do Publisher MQTT:

Execute o script publisher.py para iniciar a publicação de mensagens.


### Confirme a recepção das mensagens:

Observe o terminal do subscriber. As mensagens enviadas pelo publisher deverão aparecer, indicando que foram consumidas do tópico Kafka.


### Validação na Cloud:

Acesse a interface da Confluent Cloud e do HiveMQ Cloud para visualizar métricas e logs que confirmam o fluxo de mensagens.

# Demonstração

O Vídeo a seguir apresenta a execução do projeto e procedimentos de testes realizados:






