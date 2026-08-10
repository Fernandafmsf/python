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

