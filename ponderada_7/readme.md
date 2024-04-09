# 1 Billion Rows Challenge

# 1. Enunciado

Complete o desafio do arquivo de 1 bilhão de linhas. Só isso. Sem restrição de performance, só complete o desafio.

# Execução do Projeto

## Preparação do Ambiente

- Clone o repositório:
```
git clone https://github.com/ipatriciahonorato/modulo-9.git
cd modulo-9/ponderada_8
```
- Crie um ambiente virtual Python.

- Instale as dependências listadas no arquivo requirements.txt.

## Processamento dos Dados

- Execute o script ```createMeasurements.py``` para gerar os dados necessários. Certifique-se de ter pelo menos 12GB de espaço livre no seu sistema para acomodar os dados gerados.

``` python3 createMeasurements.py```
- Prossiga executando ```main.py``` para iniciar o processamento do desafio.

```python3 main.py``` 

# Técnicas utilizadas para solucionar o desafio

## Processamento de dados

A chave para solucionar este desafio está na eficiência da leitura e processamento dos dados. Utilizei a função ```get_data_with_txt``` para realizar a leitura dos dados de medição. A abertura do arquivo em modo binário (rb) é uma estratégia para minimizar o impacto no desempenho durante a leitura das linhas.

Durante a leitura, realizei a separação dos dados - *nome da estação e temperatura* - e os agreguei em um dicionário. Neste, a chave é o nome da estação e o valor é um array que contém, em ordem: a temperatura mínima, a temperatura máxima, a soma de todas as temperaturas registradas para a estação e a quantidade de medições realizadas. Após a leitura completa, calculei a temperatura média para cada estação usando a soma total das temperaturas e a quantidade de medições.

## Ferramentas Auxiliares
Para fornecer feedback visual durante o processamento, utilizei a biblioteca ```tqdm```. Ela gera uma barra de progresso, facilitando o acompanhamento do processo de leitura dos dados.

# Tempo de execução

O projeto levou 5.774 (346.45 segundos) minutos para ser executado, conforme mostrado abaixo:

![img 1](../ponderada_7/img/WhatsApp%20Image%202024-04-08%20at%2020.24.23.jpeg)
![img 2](../ponderada_7/img/WhatsApp%20Image%202024-04-08%20at%2020.24.24.jpeg)




