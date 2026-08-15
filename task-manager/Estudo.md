## Estudando python via projeto

### Ambiente virtualizado python 
Essa virtualização é usada em cada projeto para que possamos fazer o controle das bibliotecas/dependencias por projeto, sem haver a necessidade de instalar globalmente. 
Por exemplo, pode ser que um projeto precise de uma versão especifica de uma sistema, enquanto outro projeto vai precisar de uma versão mais atualizada. 


# Criar
python3 -m venv venv

# Ativar
source venv/bin/activate

### Variaveis, tipos e prints 
input() e output(), input usado para recolher informaçoes do usario. Vale ressaltar que toda informaçao inicialmente informada será uma string. Caso precisemos basta converter adicionando um 'int()' na frente, por exemplo 
f-string, forma de exibir uma mensagem no terminal exibindo as variaveis usando paratenteses: 
``print(f"Olá, {nome}!"")``

## Lista, tuplas e dicionarios 
list -> guarda varias coisas em ordem 
dict -> guarda infos relacionadas usando chave:valor
tuple -> guarda varios valores que, em geral, não devem ser alterados 

#### Lista
tarefas = [
    "Estudar Python",
    "Fazer exercício",
    "Estudar Git"
]
tarefas.append("Estudar SQL")


#### Dicionario
tarefa = { 
    "titulo": "Estudar Python",
    "status": "pendente"
}

Acessamos os valores pelas chaves 
print(tarefa["titulo"])

#### Lista de dicionários 
Cada tarefa é um dicionário
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

#### Tupla 
Parece uma lista, mas é imutável. Ao tentar mudar o valor da erro 
cores = ("vermelho", "azul", "verde")
cores[0] = "amarelo" -> daria erro 


### Condicionais 

#### While 
Repete um bloco enquanto a condiçao for verdadeira 


#### While true 
Muito usado para menus. True é sempre verdadeiro, criando um loop infinito. Para sair usamos um break com uma condiçao 

while True:
    resposta = input("Digite sair para parar: ")

    if resposta == "sair":
        break


#### if, else e elif 
Tomada de decisão. elif é usado para testar outra condiçao. Seria o else if. 

idade = 15

if idade >= 18:
    print("Adulto")
elif idade >= 13:
    print("Adolescente")
else:
    print("Criança")

Python verifica de cima para baixo 

### Funções 
Bloco de codigo que criamos para realizar uma funçao especifica. 

def somar(a, b):
    resultado = a + b
    return resultado

print mostra algo na tela, enquanto return devolve um valor para quem chamou a função. 


### Imports 
Para criar modulos e exportar, basta criar um novo arquivo .py, adicionar as funções nele e, para utilizar em outro arquivo, importar com from nome_arquivo import nome_funções 

