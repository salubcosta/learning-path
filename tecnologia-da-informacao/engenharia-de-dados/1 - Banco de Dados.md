## Banco de dados

Coleção de dados relacionados. Representa algum aspecto do mundo real. Finalidade específica.

## SGBD

Coleção de programas. É dependente de tecnologia. Incorpora definição, recuperação e alteração de banco de dados.

## Tipos de usuários

- Projetista de banco de dados
- Administrador de banco de dados - DBA
- Programador de aplicação
- Usuário final (leigos, casuais, avançados)
- Administrador de dados

## Linguagens do SGBD

- VDL (VIEW DEFINITION LANGUAGE)
- DDL (DATA DEFINITION LANGUAGE)
- SDL (STORAGE DEFINITION LANGUAGE)
- `DML (DATA MANIPULATION LANGUAGE)`
    - DMLs não procedurais (retornam dados, não alteram ou armazenam dados)
    - DMLs procedurais (Há alteração e armazenamento)

## Projeto de banco de dados

Natureza auto descritiva. Independência entre programas e dados.
Abstração de dados e modelo de dados. Múltiplas visões, redundãncia controlada e controle de concorrência.

`Segurança, backup e recovery, múltiplas interfaces para diferentes tipos de usuários e Manutenção de restrições de integridade`

Nível externo ou de visão > Nível conceitual > Nível interno

## Modelo hierárquico 

Os dados são estruturados hierarquicamente como uma árvore. Nó pai e nó raiz.

## Modelo em rede

Extensão do modelo hierárquico.

## Modelo relacional 

Surgiu para aumentar a independência de dados. Representa os dados em relações. É baseado na teoria dos conjuntos.

## Modelo orientado a objetos

Surgiu em decorrência das linguagens de POO.

---

Notação de Peter Chen e notação de James Martin (pé de galinha)

Medelo MER é genérico, o Diagrama DER é a materialização.

`Extensão do BD => Instância -- Intenção do BD => Esquema`

## Relacionamento

Grau de relacionamento:
- Binário: duas entidades envolvidas
- Ternário: três entidades envolvidas