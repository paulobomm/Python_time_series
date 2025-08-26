## Desvendando o Cabeçalho e a Docstring em Arquivos Python

No universo da programação em Python, a clareza e a organização do código são fundamentais. Duas ferramentas essenciais para alcançar esse objetivo, embora muitas vezes confundidas, são o **cabeçalho** do arquivo e a **docstring**. Entender a diferença entre eles é crucial para escrever um código limpo, legível e de fácil manutenção.

### O Cabeçalho: A Identidade do Arquivo

Diferente de uma `docstring`, um **cabeçalho** em um arquivo `.py` não é uma estrutura formal da linguagem Python. Trata-se de uma convenção, uma seção de comentários no início do arquivo que serve como um "cartão de visita" para o código que se segue. Geralmente, essa seção é composta por comentários de linha única, iniciados pelo caractere `#`.

**Para que serve um cabeçalho?**

O principal objetivo do cabeçalho é fornecer metadados e informações essenciais sobre o arquivo, tais como:

  * **Codificação de caracteres:** `#-*- coding: utf-8 -*-` é um exemplo clássico, garantindo que o interpretador Python entenda caracteres especiais.
  * **Shebang (Unix):** `#!/usr/bin/env python3` informa ao sistema operacional qual interpretador usar para executar o script diretamente.
  * **Informações sobre o autor e licença:** Nome do autor, data de criação, informações de contato e a licença sob a qual o código é distribuído.
  * **Breve descrição do propósito do arquivo:** Uma linha ou duas explicando o que o módulo ou script faz em um nível macro.

**Exemplo de um cabeçalho:**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# autor.py
#
# Autor:      Seu Nome
# Data:       26/08/2025
# Descrição:  Este módulo contém funções para manipulação de dados de usuários.
# Licença:    MIT
# -----------------------------------------------------------------------------
```

### A Docstring: A Documentação Integrada

A **docstring**, ou *documentation string* (string de documentação), é uma string literal que aparece como a primeira declaração em um módulo, função, classe ou método. Diferente dos comentários, a `docstring` é um objeto Python acessível em tempo de execução através do atributo especial `__doc__`. Ela é delimitada por aspas triplas (`"""` ou `'''`).

**Para que serve uma docstring?**

A principal finalidade da `docstring` é **documentar o que o objeto de código faz**. Ela é a fonte primária de informação para ferramentas de documentação automática (como o Sphinx) e para a função `help()` do próprio Python. Uma boa `docstring` explica:

  * **O propósito da função, classe ou módulo.**
  * **Os argumentos que a função ou método aceita, seus tipos e o que representam.**
  * **O que a função ou método retorna.**
  * **Quais exceções podem ser levantadas.**

**Exemplo de uma docstring em uma função:**

```python
def calcular_media(numeros):
    """Calcula e retorna a média de uma lista de números.

    Args:
        numeros (list): Uma lista de valores numéricos (int ou float).

    Returns:
        float: A média dos números na lista. Retorna 0.0 se a lista
               estiver vazia.
    """
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

# Para acessar a docstring:
print(calcular_media.__doc__)
```

### A Diferença Fundamental

| Característica | Cabeçalho do Arquivo | Docstring |
| :--- | :--- | :--- |
| **Definição** | Uma convenção de comentários (`#`) no topo do arquivo. | Uma string literal (`"""..."""`) como primeira declaração de um módulo, função, classe ou método. |
| **Propósito** | Fornecer metadados sobre o **arquivo** (autor, licença, codificação). | Documentar o **propósito e o uso** de um objeto de código específico. |
| **Acesso** | Não é diretamente acessível pelo código Python em execução. | É um atributo do objeto (`objeto.__doc__`) e pode ser acessado programaticamente e pela função `help()`. |
| **Público-alvo** | Desenvolvedores que estão lendo o código-fonte do arquivo. | Usuários da função/classe/módulo e ferramentas de documentação automática. |

Em resumo, pense no **cabeçalho** como a capa de um livro, fornecendo informações gerais sobre a obra. A **docstring**, por sua vez, é o resumo na contracapa ou o prefácio, explicando o que você encontrará dentro daquele capítulo (ou função/classe). Utilizar ambos corretamente é uma marca de um desenvolvedor Python cuidadoso e profissional.



######################################################################


# implemente as funções abaixo e coloque as docstrings

def maximo(nums):
    """oque faz
    oque recebe
    oque retorna"""
    # TODO: percorra a lista guardando o maior atual
    ...

def e_par(n: int) -> bool:
    """ ... """
    # TODO: retorne se n é par
    ...
def fatorial(n: int) -> int:
    """   ...  """
    # TODO: implemente de forma iterativa (sem recursão)
    ...
import re

def limpa_texto(s: str) -> str:
    """..."""
    # TODO: converta s para minúsculo e remova pontuações como ,.;:!?'"()-_
    ...

def conta_vogais(s: str) -> int:
    """....."""
    # TODO: conte as vogais simples
    ...

def palindromo(s: str) -> bool:
    """..."""
    # TODO: normalizar (minúsculo, remover não alfanumérico) e comparar com o reverso
    ...
