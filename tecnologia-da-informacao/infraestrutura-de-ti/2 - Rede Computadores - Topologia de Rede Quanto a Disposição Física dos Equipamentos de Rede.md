## Topologia quanto à disposição física

É a descrição da rota utilizada pelos cabos da rede para interligar nós.

## Ponto a ponto

P2P - conecta dois nós sem dispositivos intermediários

## Estrela

Há um equipamento central. Nós são conectados por cabos a um componente centralizado (Hub/Switch) para chavear a comunicação. Essa comunicação se dá através de endereço de rede.

- Vantagens
    - Facilidade em isolar a fonte de uma falha
    - Baixo investimento
    - Facilidade de inclusão de nova estação
- Desvantagem
    - Confiabilidade (uma falha no concentrador sem redundância para a rede)
    - Tráfego intenso pode representar ponto de congestionamento

## Anel ou ring

Cada dispositivo está conectado ao próximo formando um círculo fechado.

Características: 
- Cada dispositivo tem dois dispositivos conectados
- Dados circulam pelo anel
- Podem usar token
- Não há concentrador

Vantagens
- organização simples e estruturada
- Evita colisões

desvantagem:
- adicionar novos dispositivos

## Barra

Forma de organização todos os nós compartilham o único cabo central. Canal de comunicação compartilhado.

Características:
- Unidirecional

Vantagem:
- Fácil de instalar
- Baixo custo

## Árevore

Combina estrela e barramento. 

## Mista ou híbrida

Combina duas ou mais topologias básicas. Permite flexibilidade e escalabilidade. Maior complexidade de gerenciamento.