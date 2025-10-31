## Arquitetura de Software

Surgiu devido aos projetos de software ficarem maiores e mais complexos.

## Arquitetura monolítica 

Surgiu 1970 e foi consolidada em 1980. Objetivos foi simplificar o desenvolvimento e implementação. 

## Arquitetura cliente-servidor

Surgiu em 1980. Objetivo é distribuir carga de trabalha. Cliente parte do usuário e servidor é onde ocorre o processamento.

## Arquitetura OO

1980, objetiva desenvolver de uma forma que imita o mundo real. Há objetos e classes.

## MVC

1970 e consolidada em 1990. Há três camadas: Model, view e Controller.

## Arquitetura em camadas

1980 e consolidada em 1990. Organiza o desenvolvimento em camadas. Apresentação, regras de negócios e dados.

## Arquitetura de objetos distribuídos

1980, consolidada em 1990. Objetos em diferentes máquimas mas funciona como se estivesse em um único lugar.

## SOAP

Permitir comunicação distribuída. XML

## P2P

Nós atuam como clientes e servidores ao mesmo tempo.

## SOA

Diferente serviço interaja e funcione juntos. Serviços distintos, interfaces bem definidas e fazendo uso de protocolos de comunicação 

## REST

Criar APIs e utiliza os métodos HTTP (get, post, put, delete e patch)

## Arquitetura Event-Driven

Reage a eventos

## Hexagonal

Um núcleo com diversos adaptadores, portas e comunicação sem se preocupar com a tecnologia externa ao núcleo.
Um dos principais objetivos é isolar o núcleo da aplicação externa.

- Núcleo da Aplicação
    - Núcleo é o coração do sistema, responsável pela lógica de negócios.
    - Classes de domínio representam principais conceitos do negócio.
- Portas
    - São interfaces que define como vai ser a comunição entre o núcleo da aplicação e o mundo externo.
    - Inbound ports - permitem entradas de dados
    - Outbound ports - saída de dados para fora do núcleo
- Adaptadores
    - Traduz chamadas do núcleos para as tecnologias externas e vice-versa
    - Inbound adapter - conectam a interface do usuário ao núcleo da aplicação
    - Outbound adapter - conecta o núcleo da aplicação ao mundo externo