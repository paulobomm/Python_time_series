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

---------------------------------------------------------------------------------------------

"""
text_utils.py

import re


def maximo(nums: Iterable[Number]) -> Optional[Number]:
    """Retorna o maior valor de um iterável de números.

    Percorre o iterável comparando itens e mantém o maior atual.

    Args:
        nums: Iterável de valores numéricos (int ou float).

    Returns:
        O maior número encontrado ou None se o iterável estiver vazio.

    Examples:
        >>> maximo([])
        >>> maximo([1])
        1
        >>> maximo([-5, -2, -10])
        -2
        >>> maximo([1, 2.5, 2])
        2.5
    """
    iterator = iter(nums)
    try:
        maior = next(iterator)
    except StopIteration:
        return None

    for valor in iterator:
        if valor > maior:
            maior = valor
    return maior


def e_par(n: int) -> bool:
    """Verifica se um número inteiro é par.

    Args:
        n: Número inteiro a ser verificado.

    Returns:
        True se n for par; False caso contrário.

    Examples:
        >>> e_par(0)
        True
        >>> e_par(7)
        False
        >>> e_par(-4)
        True
    """
    return (n % 2) == 0


def fatorial(n: int) -> int:
    """Calcula o fatorial de um número de forma iterativa (sem recursão).

    Args:
        n: Inteiro não negativo.

    Returns:
        O valor de n! (fatorial de n).

    Raises:
        TypeError: Se n não for int.
        ValueError: Se n for negativo.

    Examples:
        >>> fatorial(0)
        1
        >>> fatorial(1)
        1
        >>> fatorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("fatorial: 'n' deve ser int.")
    if n < 0:
        raise ValueError("fatorial: não definido para números negativos.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def limpa_texto(s: str) -> str:
    """Converte `s` para minúsculo e remove pontuações básicas.

    Remove os caracteres: , . ; : ! ? ' " ( ) - _

    Obs.: Mantemos espaços; se desejar normalizar espaços também,
    use `re.sub(r"\\s+", " ", texto).strip()` após esta função.

    Args:
        s: Texto de entrada.

    Returns:
        Texto em minúsculo sem as pontuações listadas.

    Examples:
        >>> limpa_texto("Olá, Mundo!!!")
        'olá mundo'
        >>> limpa_texto("A-b_c(d)e")
        'ab cde'
    """
    texto = s.lower()
    # Remoção direta das pontuações definidas; preserva outros sinais (como acentos).
    texto = _PONTUACAO_RE.sub("", texto)
    return texto


def conta_vogais(s: str) -> int:
    """Conta vogais simples (a, e, i, o, u) no texto.

    A contagem é *case-insensitive* e não considera acentos (ex.: 'á' não é contado).
    Para contar vogais acentuadas também, ajuste o conjunto de vogais conforme sua regra.

    Args:
        s: Texto de entrada.

    Returns:
        Quantidade de vogais simples.

    Examples:
        >>> conta_vogais("Python")
        1
        >>> conta_vogais("aeiou AEIOU")
        10
        >>> conta_vogais("áéíóú")
        0
    """
    vogais = {"a", "e", "i", "o", "u"}
    return sum(1 for ch in s.lower() if ch in vogais)


def palindromo(s: str) -> bool:
    """Verifica se um texto é palíndromo, ignorando caixa e não-alfanuméricos.

    A normalização aplicada:
      - `casefold()` para comparação sem distinção de maiúsculas/minúsculas
      - filtro `str.isalnum()` para manter apenas caracteres alfanuméricos (Unicode)

    Args:
        s: Texto a ser verificado.

    Returns:
        True se `s` for palíndromo após normalização; False caso contrário.

    Examples:
        >>> palindromo("ana")
        True
        >>> palindromo("Roma é amor")
        True
        >>> palindromo("Python")
        False
        >>> palindromo("Socorram-me, subi no ônibus em Marrocos")
        True
    """
    norm = "".join(ch for ch in s.casefold() if ch.isalnum())
    return norm == norm[::-1]
