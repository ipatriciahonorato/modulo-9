# Teste de um simulador de dispositivos IoT
## 1. Enunciado
Utilizando o simulador de dispositivos IoT desenvolvido na atividade passada e utilizando os conceitos de TDD vistos no decorrer da semana, implemente testes automatizados para validar o simulador. Seus testes obrigatoriamente devem abordar os seguintes aspectos:

- Recebimento - garante que os dados enviados pelo simulador são recebidos pelo broker.
- Validação dos dados - garante que os dados enviados pelo simulador chegam sem alterações.
- Confirmação da taxa de disparo - garante que o simulador atende às especificações de taxa de disparo de mensagens dentro de uma margem de erro razoável.

# Descrição do Projeto

Este projeto tem como objetivo implementar testes automatizados para um simulador de dispositivos IoT desenvolvido anteriormente, utilizando os conceitos de Test-Driven Development (TDD) para garantir a qualidade e a eficácia do simulador. Os testes abordam aspectos críticos como recebimento e validação dos dados enviados pelo simulador, além da confirmação da taxa de disparo de mensagens, conforme especificado.

## Tecnologias Utilizadas
- **Linguagem de Programação:** Python
- **Biblioteca MQTT:** Eclipse Paho MQTT Python Client
- **Framework de Teste:** unittest (Python Standard Library)

## Instalação e Configuração

### Clonar o Repositório
Para obter o código do projeto, incluindo o simulador e os testes, clone o repositório do GitHub.

        git clone <https://github.com/ipatriciahonorato/modulo-9.git>
	    cd <ponderada-2>
### Configuração do Ambiente Virtual
Recomenda-se a utilização de um ambiente virtual para instalar as dependências. Para criá-lo e ativá-lo:

    python3 -m venv venv
    source venv/bin/activate
## Funcionalidades Principais

1. **Setup do Subscriber para Testes** A função `setup_subscriber` configura o cliente MQTT para atuar como subscriber, armazenando as mensagens recebidas para validação posterior nos testes.

`def setup_subscriber():
    def on_message(client, userdata, message):
        received_messages.append(message.payload.decode())`

    subscriber = mqtt.Client()
    subscriber.on_message = on_message
    subscriber.connect(broker, port)
    subscriber.subscribe(topic)
    subscriber.loop_start()
    return subscriber

2. **Teste de Recebimento dos Dados** O método `test_data_reception` verifica se uma mensagem enviada pelo publisher é corretamente recebida pelo broker.

    `def test_data_reception(self):
        test_message = "Test message"
        publisher.publish(topic, test_message)
        time.sleep(2)
        self.assertIn(test_message, received_messages)`

3. **Teste de Validação dos Dados** O método `test_data_validation` assegura que os dados recebidos correspondem exatamente aos dados enviados.

    `def test_data_validation(self):
        self.assertEqual(received_messages[-1], "Test message")`

4. **Teste da Taxa de Disparo de Mensagens** O método `test_message_dispatch_rate` valida se o simulador está disparando mensagens dentro da taxa especificada.

`def test_message_dispatch_rate(self):
    start_time = time.time()
    for _ in range(2):
        publisher.publish(topic, "Rate test message")
        time.sleep(5)
    duration = time.time() - start_time
    self.assertTrue(9 <= duration <= 11)`

## Executando os Testes
Para executar os testes automatizados e validar o funcionamento do simulador, use o seguinte comando:

`pytest`

Este comando busca e executa todos os testes dentro do diretório especificado, garantindo que todas as funcionalidades do simulador sejam testadas conforme os critérios estabelecidos.

## Vídeo demonstrativo
[![O vídeo a seguir apresenta a execução dos testes desse projeto](https://i3.ytimg.com/vi/XoXG-HeK4d0/maxresdefault.jpg)](https://youtu.be/XoXG-HeK4d)

## Referências e Material de Estudo
- Eclipse Paho MQTT Python Client: [Documentação Oficial](https://eclipse.dev/paho/index.php?page=clients/python/index.php)
- unittest — Unit testing framework: [Documentação Python](https://docs.python.org/3/library/unittest.html)
- Tutorial de Testes em Python: [Material de estudo fornecido pelo professor](https://rmnicola.github.io/m9-ec-encontros/tdd-python), que cobre a criação de pacotes Python e a implementação de testes unitários utilizando as melhores práticas de TDD.


   

