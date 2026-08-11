
# height = 1.65
# studying = True

# age = int(input("What is your age? ")) ## Convertendo a string para inteiro
# print(name)
# print(age)
# print(height)
# print(studying)
# print(type(name))

name = input("What is your name? ") ## Tudo que vem de input, inicialmente será uma string
print(f"Hello {name}! Welcome!")

## Listas
tarefas = [ 
    "Estudar python",
    "Fazer exercicios", 
    "Estudar git",
]

print(f"Essa é uma lista: {tarefas}")

tarefas.append("Estudar SQL") ## Adicionando um item na lista
print(f"Essa é a lista atualizada: {tarefas}")

## Dict
task ={ 
    "title": "Estudar python",
    "status": "Em andamento",
}
print(f"Esse é um dict: {task}")
print(task["title"]) ## Acessando o valor de uma chave do dicionário
task["status"] = "Concluida"
print(task)

## Lista de dicionarios
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

## Tupla 
cores = ("azul", "vermelho", "verde") ## Tuplas são imutáveis
