#  Integração do Simulador com HiveMQ

# 1. Enunciado
Nessa atividade, deve-se desenvolver a integração entre o simulador desenvolvido nas duas primeiras atividades ponderadas e um cluster configurado no HiveMQ. Para tal, deve-se garantir que o simulador é capaz de se comunicar utilizando autenticação em camada de transporte (TLS).

# Descrição do Projeto

Este projeto visa integrar um simulador desenvolvido em Python com um cluster do HiveMQ, utilizando a autenticação em camada de transporte (TLS) para garantir uma comunicação segura. O simulador simula dados de um sensor SPS30, gerando valores de concentrações de massa e número de partículas, que são enviados ao broker MQTT do HiveMQ.

## Tecologias

##  Instalação e Configuração do Projeto

### Requisitos
- Python 3.8 ou superior
- Variáveis de ambiente ou arquivo .env para as credenciais do HiveMQ

### Passo a Passo:

1. Clone o repositório:
```
   git clone <https://github.com/ipatriciahonorato/modulo-9.git>
    cd <ponderada-4>
```
2. Instale as dependências
```
pip install .
```
3. Configure um Cluster no HiveMQ e salve suas credenciais de acesso.
  
5. Configure as credenciais do HiveMQ. Você pode fazer isso de duas maneiras:

- Localmente: Crie um arquivo .env no diretório raiz do projeto ou altere o arquivo .bashrc com o seguinte conteúdo:
```
MQTT_BROKER=2fe1c52b706f4de7bc673787cd26080e.s1.eu.hivemq.cloud
MQTT_PORT=8883
MQTT_TOPIC=sps30/topic
MQTT_CLIENT_ID_PUBLISHER=python_publisher_test
MQTT_CLIENT_ID_SUBSCRIBER=python_subscriber_test
MQTT_USERNAME= id username
MQTT_PASSWORD= password
```
- No GitHub: Adicione as mesmas variáveis de ambiente como Secrets no seu repositório GitHub para uso no GitHub Actions.

## Funcionalidades Principais

### publisher.py
Este script é responsável por simular dados de um sensor de qualidade do ar (SPS30) e publicá-los em um tópico MQTT no broker HiveMQ.

**Funcionalidades e Funções:**

**Configuração Inicial:**

- Importação das bibliotecas necessárias.
- Leitura das variáveis de ambiente para a configuração do broker MQTT, incluindo o endereço do broker, porta, nome de usuário e senha.


1. generate_sps30_data():

- Esta função simula a geração de dados do sensor SPS30, criando valores aleatórios para concentrações de massa (PM1.0, PM2.5, PM4.0, PM10) e concentrações de número de partículas. Ela retorna uma mensagem formatada com esses valores.

2. Conexão e Publicação:

- Criação de uma instância do cliente MQTT com configurações de TLS e autenticação usando as credenciais fornecidas.
Conexão ao broker MQTT.
- Loop infinito que gera dados simulados usando ```generate_sps30_data()``` e publica esses dados no tópico MQTT configurado, com um intervalo definido entre publicações.


### subscriber.py
- Este script atua como um assinante MQTT, recebendo mensagens publicadas em um tópico específico no broker HiveMQ.

**Funcionalidades e Funções:**

**Configuração Inicial:**

- Similar ao publisher.py, ele carrega as configurações do broker MQTT a partir de variáveis de ambiente.
  
1. Callbacks:
- on_connect(): Função chamada quando o cliente se conecta (ou reconecta) ao broker MQTT. Ela verifica se a conexão foi bem-sucedida e se inscreve em um tópico MQTT.
- on_message(): Função chamada quando uma mensagem é recebida no tópico subscrito. Ela imprime a mensagem recebida.
  
2. Conexão e Escuta:
- Criação e configuração do cliente MQTT com TLS e autenticação.
- Conexão ao broker MQTT e início do loop para escutar por mensagens de forma contínua.
  
### test_simulador.py

- Este script contém testes unitários para verificar a funcionalidade do simulador e sua integração com o HiveMQ.

**Funcionalidades e Funções:**

**Configuração dos Testes:**

- Carregamento das configurações de conexão MQTT a partir de variáveis de ambiente.
- Definição de uma função tls_set() para configurar a conexão TLS do cliente MQTT nos testes.

1. setup_subscriber():

- Prepara um assinante MQTT para os testes, configurando callbacks para capturar mensagens recebidas.

2. Classe TestIoTSimulator:

- setUpClass(): Método chamado antes de executar os testes da classe, configurando o ambiente de teste.
- tearDownClass(): Método chamado após todos os testes da classe terem sido executados, para limpar o ambiente de teste.
  
3. Testes:
- test_data_reception(): Verifica se os dados podem ser recebidos corretamente pelo assinante.
- test_data_validation(): Confirma se os dados recebidos correspondem aos dados enviados.
- test_message_dispatch_rate(): Testa se as mensagens estão sendo enviadas na taxa esperada.

## Testes 

### Execução Local

Para executar os testes localmente, use o comando:

```
pytest
```

### Testes Automatizados no GitHub Actions:

Os testes também são automatizados via GitHub Actions, assegurando que cada push ou pull request para a branch main execute os testes automaticamente, utilizando as credenciais configuradas nos Secrets do repositório.

## Conclusão

Este projeto atende aos critérios estabelecidos na descrição da ponderada, com a integração bem-sucedida ao cluster HiveMQ usando TLS, a demonstração do funcionamento por meio de scripts de publicador e assinante, e a implementação de testes automatizados, tanto localmente quanto via GitHub Actions, para validar a integração.

## Demonstração do Projeto

[![O vídeo a seguir apresenta a execução dos testes e integração desse projeto](https://i3.ytimg.com/vi/VesROpWxc5Y/maxresdefault.jpg)](https://youtu.be/VesROpWxc5Y)



