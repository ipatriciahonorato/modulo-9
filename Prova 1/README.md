# Prova 1

## Nome: Patricia Honorato Moreira


Este projeto consistiu no desenvolvimento de um sistema de monitoramento de umidade para estufa, com diferentes componentes:

### Publicação de Dados de Umidade (publisher.py):

- Gera dados simulados de umidade para sensores de hortaliças e flores.
- Publica esses dados em tópicos MQTT específicos para cada sensor.
- Utiliza a biblioteca paho.mqtt.client para comunicação MQTT.

### Assinatura de Dados de Umidade (subscriber.py):

- Assina tópicos MQTT específicos para receber dados de umidade.
- Imprime os dados recebidos e os exibe no console.
- Utiliza a biblioteca paho.mqtt.client para comunicação MQTT.

### Interface Gráfica de Monitoramento de Umidade (interface.py):

- Cria uma interface gráfica usando PyQt5 para exibir os dados de umidade em tempo real.
- Atualiza os dados periodicamente utilizando um timer.
- Utiliza a biblioteca PyQt5 para criar a interface gráfica.

### Testes Unitários (PyTDD):

- Testa a funcionalidade do sistema, incluindo a recepção correta de mensagens MQTT com QoS 1, integridade das mensagens recebidas e o funcionamento dos alarmes de umidade.
- Utiliza a biblioteca unittest para escrever os testes e paho.mqtt.client para comunicação MQTT nos testes.

## Video demonstrativo

O vídeo abaixo apresenta o funcionamento do sistema de monitoramento:

[Link do vídeo!](https://youtu.be/DoXfdNgPchA)



