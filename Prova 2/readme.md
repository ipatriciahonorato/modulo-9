# PROVA 2 

### Nome: Patricia Honorato Moreira

### Turma: 3° ano de Engenharia da Computação no Inteli

## Critérios

- **Implementar um Producer (Produtor):** Deve coletar dados simulados de sensores de qualidade do ar e publicá-los em um tópico do Kafka chamado qualidadeAr. Os dados devem incluir:
```Id do sensor, timestamp, tipo de poluente e nivel da medida.```

- **Implementar um Consumer (Consumidor):** Deve assinar o tópico qualidadeAr e processar os dados recebidos, exibindo-os em um formato legível, além de armazená-los para análise posterior (escolha a forma de armazenamento que achar mais adequada).

- **Implementar testes de Integridade e Persistência:** Criar testes automatizados que validem a integridade dos dados transmitidos (verificando se os dados recebidos são iguais aos enviados) e a persistência dos dados (assegurando que os dados continuem acessíveis para consulta futura, mesmo após terem sido consumidos).


## Setup Local


A configuração do cluster kafka local foi feita conforme o tutorial do professor: [Tutorial - Setup de um cluster Kafka local
](https://rmnicola.github.io/m9-ec-encontros/kafka-setup)


## Componentes do Projeto


### Arquivo ``docker-compose.yml``

Este arquivo é usado para definir e rodar a infraestrutura de serviços Kafka com o Docker Compose. O arquivo contém a configuração para dois serviços Zookeeper e dois serviços Kafka.

- Zookeeper: É configurado com dois nós para gerenciar a coordenação do cluster Kafka. Eles escutam na porta padrão 2181, mapeada para as portas 22181 e 32181 no host.

- Kafka: São configurados dois brokers Kafka, que dependem dos serviços Zookeeper. C Eles expõem as portas 29092 e 39092 no host, mapeadas a partir da porta interna 9092.

### Arquivo ``consumer-kafka.py``

É responsável por ler as mensagens do tópico qualidadeAr. As mensagens são formatadas de JSON para um formato Python e exibidas de forma legível. O consumidor também salva as mensagens formatadas em um arquivo chamado ``sensor_data.txt.``

Funcionalidades principais:

- Processa mensagens e formata os dados recebidos, os exibindo no terminal.
- Persistência de dados: armazenada as mensagens em um arquivo de texto. 

### Arquivo ``producer-kafka.py``

É  responsável por simular dados de sensores de qualidade do ar e publicá-los no tópico qualidadeAr. O produtor gera mensagens que incluem informações como ID do sensor, timestamp, tipo de poluente e nível de poluição.

Funcionalidade principal:

- Envia os dados em loop a cada cinco segundos, simulando um fluxo contínuo de dados de sensor.

## Teste de Persistência de dados 

Para validação dos testes, foi criada uma função dentro do ``consumer-kafka.py`` que cria o arquivo ``sensor_data.txt``. Esse arquivo funciona da seguinte maneira:

- Após o consumidor processar as mensagens, o arquivo de texto deve ser preenchido com os novos dados.
- O arquivo não perde as entradas anteriores e não as sobrepoe os dados já salvos, mesmo após o Kafka ser reiniciado.
- O arquivo pode ser aberto e lido a qualquer momento da execução do projeto e mostra os dados sendo recebidos.
- Os dados estão de acordo com o que é mostrado no terminal e na interface do consumer no Kafka.

## Execução do projeto

1. Inicialização do Cluster Kafka Local

Utilize o comando:

``flatpak run io.conduktor.Conduktor``

2. Execução do producer e consumer:

``python3 consumer-kafka.py``
``python3 producer-kakfa.py``


## Visuazaliação do Projeto

Os dados podem ser observados no terminal, Kafka e também no arquivo sensor_data.txt.

## Vídeo demonstrativo do sistema

O vídeo abaixo apresenta uma simulação do projeto em funcionamento e a persistência de dados do sistema.

https://youtu.be/CzFDrgyhxMY

[![O vídeo a seguir apresenta a integração desse projeto](https://i3.ytimg.com/vi/CzFDrgyhxMY/maxresdefault.jpg)](https://youtu.be/CzFDrgyhxMY)

Imagem Tópico qualidadeAr:

[topico](https://github.com/ipatriciahonorato/modulo-9/blob/main/Prova%202/topico.png)



