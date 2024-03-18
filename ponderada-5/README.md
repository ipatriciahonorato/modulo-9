# Integração do simulador com Metabase

## 1. Enunciado

Nessa atividade, deve-se desenvolver a integração entre o simulador desenvolvido nas três primeiras atividades e um dashboard desenvolvido usando o Metabase, com persistência de dados em um banco de dados a sua escolha.

## Descrição do Projeto

Este projeto consiste em um sistema de monitoramento da qualidade do ar que utiliza a tecnologia MQTT para coletar dados de sensores de partículas, como PM1.0, PM2.5, PM4.0, e PM10, além de suas concentrações numéricas. Os dados são gerados por um simulador, publicados em um tópico MQTT, e depois consumidos por um serviço de assinatura que armazena essas informações em um banco de dados MongoDB para persistência. 

## Componentes do Sistema

### Simulador de Dados de Sensores ```(publisher.py)```
O simulador de dados, implementado em Python, simula a coleta de dados de qualidade do ar por sensores reais. Através de valores aleatórios dentro de um intervalo pré-definido, o simulador gera medições de diferentes tipos de partículas (PM1.0, PM2.5, PM4.0, PM10, e suas concentrações numéricas). Esses dados são convertidos em um formato JSON e publicados em um tópico MQTT específico, simulando o comportamento de sensores de qualidade do ar em um ambiente real.

### Serviço de Assinatura MQTT ```(subscriber.py)```
O serviço de assinatura é responsável por receber os dados publicados no tópico MQTT. Ao assinar o tópico de interesse, esse serviço utiliza a biblioteca Paho MQTT para estabelecer uma conexão segura com o broker MQTT, recebendo os dados em tempo real. Após a recepção, os dados são armazenados em uma coleção específica dentro de um banco de dados MongoDB, garantindo a persistência e organização das informações coletadas para análises futuras.

### Banco de Dados MongoDB
MongoDB é utilizado como sistema de armazenamento de dados devido à sua flexibilidade e capacidade de lidar com grandes volumes de dados estruturados em formato JSON. O banco de dados ponderada_4 e a coleção sensor armazenam os registros de dados recebidos.

### Visualização e Análise de Dados com Metabase
Metabase é uma ferramenta de inteligência de negócios (BI) que permite a visualização interativa e a análise dos dados armazenados no MongoDB. Após configurar a conexão entre o Metabase e o MongoDB, os usuários podem criar dashboards personalizados, gráficos e relatórios que destacam insights sobre a qualidade do ar. 

## Instalação e Configuração do Projeto

## Pré-requisitos
- Docker instalado em sua máquina;
- MongoDB Compass instalado na máquina;

### Após isso, siga os seguintes passos:

**1. Clone o repositório:**

```
   git clone <https://github.com/ipatriciahonorato/modulo-9.git>
    cd <ponderada-5>
```

**2. Crie um ambiente virtual para os scripts** ```publisher.py``` e ```subscriber.py```

**3. Uso do Docker para Inicialização do MongoDB**

Para inicializar uma instância do MongoDB usando o Docker, execute o seguinte comando. Isso vai baixar a imagem do MongoDB (se ainda não estiver localmente disponível) e iniciar um container do MongoDB.

```
docker run --name mongodb -d -p 27017:27017 mongo
```

Este comando cria e inicia um container chamado mongodb que executa a versão mais recente do MongoDB. O container expõe a porta 27017, permitindo conexões ao banco de dados.

Após isso, crie seu banco de dados no MongoDB Compass. 


## Execução do Projeto

**1. Execute os scripts ```publisher.py``` e ```subscriber.py``` para envio de dados para o banco de dados**

**2. Acesso ao Metabase com Docker com persistência de dados**

Para o Metabase, execute o seguinte comando para iniciar o Metabase em um container Docker, conectando-o à rede do host para permitir o acesso ao MongoDB que está rodando localmente ou em outro container.

```
docker run -d -p 3000:3000 \
    -v /home/patricia/meu_workspace/modulo-9/ponderada-5/metabase-data:/metabase.db \
    --name metabase --network="host" metabase/metabase
```

Este comando realiza o seguinte:

- -d executa o container em modo detach (em segundo plano).
- -p 3000:3000 mapeia a porta 3000 do container para a porta 3000 do host.
- -v /home/patricia/meu_workspace/modulo-9/ponderada-5/metabase-data:/metabase.db monta um volume para persistência dos dados do Metabase.
- --network="host" configura o container para usar a rede do host, permitindo que o Metabase acesse o MongoDB que está rodando no host ou em outro container.
- metabase/metabase é a imagem que será utilizada para criar o container.

*Observação: Ao utilizar o --network="host", as configurações de portas (-p) são ignoradas, pois o container está utilizando diretamente a rede do host.*


Após a inicialização do container do Metabase, acesse o Metabase em **http://localhost:3000**(ou outro endereço configurado) no seu navegador. Siga o assistente de configuração para conectar o Metabase ao MongoDB.

**3. Visualizar e Analisar os Dados**

Utilize o Metabase para criar dashboards, gráficos e relatórios baseados nos dados de qualidade do ar coletados, facilitando a análise e o monitoramento em tempo real.

