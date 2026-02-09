 # Introdução à Python e POO
 
 ## Conceitos básicos - Aula 01

- Que história é essa? 
<p>
 Python foi criada em 1980 por Guido Van Rossum com o objetivo de ser uma linguagem de programação interpretada c/ comandos simples e fácil de entender.
</p>

<p> 
 Os códigos da aula 1 estarão dentro do arquivo <code>poo_aula_01.ipynb</code>
</p>

## Os 4 Pilares da Orientação a Objetos - Aula 02

- Que história é essa? 
<p>
 Programação procedural é baseada em conceitos de chamadas a procedimentos, já a programação orientada a objetos é uma aproximação da visão que temos do mundo.
</p>

`Na POO as classes estão para objetos assim como as formas estão para bolos`

<p> 
 Os códigos da aula 2 estarão dentro do arquivo <code>poo_aula_02.ipynb</code>
</p>

## Boas práticas de OO e de codificação em Python - Aula 03

### Princípios SOLID:
<p>

- S (single responsibility principle (SPR)) - Princípio de responsabilidade única
  - Uma classe deve ser especializada em um único assunto e ter apenas uma responsabilidade dentro do software
- O (open/closed principle (OCP)) - Princípio do aberto/fechado
  - A classe deve estar aberta para extensão, porém fechada para modificação
- L (liskov substitution principle (LSP)) - Princípio de substituição de Liskov
  - Uma subclasse deve poder ser substituída pela sua superclasse
- I (interface segregation principle (ISP)) - Princípio de segregação de interface
  - Este princípio define que várias interfaces específicas são melhores do que uma interface genérica
- D (dependency inversion principle (DIP)) - Princípio da inversão de dependência
  - Define que devemos depender de abstrações, e não de implementações

</p>

<p>
Será abordado os códigos com exemplos dos princípios SOLID no arquivo: <code>poo_aula_03.ipynb</code>
</p>

### Guia de Estilos

<p> 
O criador do Python - Guido Von Rossum - é o principal autor do guia de estilos da linguagem Python.

PEP (Python Enhancement Proposal) são documentos técnicos que definem novas funcionalidades, padrões de design e diretrizes de estilo para a linguagem Python.

Conforme descrito na PEP-1, as PEPs podem ser:

- de padrões
- informacionais
- de processos

Todas as PEPs estão aqui: [PEPs](https://peps.python.org/pep-0000/)
</p>

### Nomenclatura

- função:
  - use uma palavra minúscula, separada por sublinhados (_), exemplo: function, my_function
- variável:
  - use uma letra, palavra, palavras, minúsiculas separadas por sublinhados (_), exemplo: x, var, my_variable
- classe:
  - CamelCase, exemplos: Model, MyClass
- método:
  - snake_case, exemplo: class_method(), save_all()
- constante:
  - tudo maiúsculo e separado por sublinhado (_), CONSTANTE, MY_CONSTANT, BASE_URL
- módulo:
  - tudo minúsculo e separado por sublinhado (_), module.py, my_modulo.py
- pacote:
  - tudo minúsculo e não há separação, exemplo: package, mypackage

<p>
Será abordado os códigos com exemplos de boas práticas no arquivo: <code>poo_aula_03_boas_praticsa.ipynb</code>
</p>