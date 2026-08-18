# Estudando Python via Projeto

## Ambiente Virtualizado Python

Essa virtualização é usada em cada projeto para controlar as bibliotecas/dependências por projeto, sem instalar globalmente.
Por exemplo, um projeto pode precisar de uma versão específica de uma biblioteca, enquanto outro precisa de uma versão mais atualizada.

```bash
# Criar
python3 -m venv venv

# Ativar
source venv/bin/activate
```

---

## Variáveis, Tipos e Prints

- `input()` é usado para recolher informações do usuário. Toda informação recebida será uma `string` por padrão. Para converter, basta envolver com `int()`, por exemplo.
- **f-string**: forma de exibir variáveis em mensagens no terminal usando chaves:

```python
print(f"Olá, {nome}!")
```

---

## Listas, Tuplas e Dicionários

| Tipo    | Descrição                                              |
|---------|--------------------------------------------------------|
| `list`  | Guarda vários valores em ordem                         |
| `dict`  | Guarda informações relacionadas usando `chave: valor`  |
| `tuple` | Guarda vários valores que, em geral, não devem ser alterados |

### Lista

```python
tarefas = [
    "Estudar Python",
    "Fazer exercício",
    "Estudar Git"
]
tarefas.append("Estudar SQL")
```

### Dicionário

```python
tarefa = {
    "titulo": "Estudar Python",
    "status": "pendente"
}

# Acessamos os valores pelas chaves
print(tarefa["titulo"])
```

### Lista de Dicionários

```python
# Cada tarefa é um dicionário
tarefas = [
    {
        "titulo": "Estudar Python",
        "status": "pendente"
    },
    {
        "titulo": "Fazer exercício",
        "status": "concluída"
    }
]

tarefas.append({
    "titulo": "Fazer exercício",
    "status": "concluída"
})
```

### Tupla

Parece uma lista, mas é imutável — ao tentar alterar um valor, ocorre um erro.

```python
cores = ("vermelho", "azul", "verde")
cores[0] = "amarelo"  # TypeError: 'tuple' object does not support item assignment
```

---

## Condicionais

### `while`

Repete um bloco enquanto a condição for verdadeira.

### `while True`

Muito usado para menus. `True` é sempre verdadeiro, criando um loop infinito. Para sair, usamos `break` com uma condição.

```python
while True:
    resposta = input("Digite sair para parar: ")

    if resposta == "sair":
        break
```

### `if`, `else` e `elif`

Tomada de decisão. `elif` testa outra condição (equivalente ao `else if`). Python verifica as condições de cima para baixo.

```python
idade = 15

if idade >= 18:
    print("Adulto")
elif idade >= 13:
    print("Adolescente")
else:
    print("Criança")
```

---

## Funções

Bloco de código criado para realizar uma tarefa específica.

```python
def somar(a, b):
    resultado = a + b
    return resultado
```

> `print` mostra algo na tela, enquanto `return` devolve um valor para quem chamou a função.

---

## Imports

Para criar módulos, basta criar um novo arquivo `.py` e adicionar as funções nele. Para usar em outro arquivo, importe com:

```python
from nome_arquivo import nome_funcao
```

