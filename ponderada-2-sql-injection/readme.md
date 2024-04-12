## Nomes: Patricia Honorato Moreira, Luiz Fernando da Silva Borges e Alysson C.C. Cordeiro.

## Ponderada 2 - Professor Rafael - Avaliação de Segurança do Projeto


### Matriz de Impacto x Probabilidade (Avaliação de Segurança do Projeto)


A matriz de impacto x probabilidade que desenvolvemos contém uma análise detalhada de quatro vulnerabilidades críticas identificadas em sistemas MQTT, cada uma abordada com sua respectiva probabilidade de ocorrência, impacto no sistema, e estratégias de mitigação sugeridas. Vamos detalhar o que cada parte da matriz representa:

| Vulnerabilidade | Probabilidade | Impacto | Mitigação |
|-----------------|---------------|---------|-----------|
| **Uso Compartilhado de ClientIDs** | Alta | Alto | Implementação de políticas de segurança que proíbam o uso compartilhado de ClientIDs entre múltiplas sessões. Isso inclui a garantia de autenticação única e verificação rigorosa para cada conexão, visando proteger a confidencialidade das comunicações ao impedir que mensagens possam ser interceptadas ou acessadas por usuários não autorizados. |
| **Ausência de Autenticação para Publicação** | Alta | Muito Alto | Necessidade de exigir autenticação forte e verificável para todos os clientes que desejam publicar mensagens no broker MQTT. Isso pode ser alcançado através de mecanismos como tokens de acesso, certificados digitais ou autenticação baseada em desafio-resposta, com o objetivo de prevenir a inserção não autorizada de mensagens que poderiam comprometer a integridade dos dados no sistema. |
| **Carga Intensa Levando à Indisponibilidade** | Média | Alto | Implementação de mecanismos robustos de controle de carga e rate limiting para gerenciar o volume de mensagens, evitando assim a sobrecarga dos servidores. Isso pode incluir a autenticação e verificação das fontes de tráfego, além da capacidade de escalonamento horizontal do sistema, para manter a disponibilidade do serviço mesmo sob condições de uso intenso. |
| **SQL Injection em Interfaces de Administração** | Média | Muito Alto | Adoção de práticas de desenvolvimento seguro específicas para prevenir a vulnerabilidade de SQL Injection, especialmente em interfaces web de administração que interagem com bancos de dados. Isso envolve a sanitização rigorosa de todas as entradas de usuário, uso de prepared statements e procedures armazenadas para consulta aos bancos de dados, garantindo assim a integridade e a segurança dos dados manipulados. |

Essa matriz proporciona uma visão clara das principais ameaças à segurança de sistemas baseados em MQTT, priorizando ações para reforçar a segurança e a resiliência desses sistemas frente a ataques cibernéticos.



