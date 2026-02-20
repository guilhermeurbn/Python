#aula 07



def find(lista, valor):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            return True
        i += 1
    return (False)

def lugar(lista, valor):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            return i
        i += 1

lista = ["guilherme", 22, "milena", 20, "jonh", 23]


i = 0
novo_usuario = input("gostaria de atualizar o nome ou a idade: ")

while(1):
    if "nome" in novo_usuario:
        old_name = input("qual seu nome atual: ")
        if find(lista, old_name):
            lista[lugar(lista, old_name)] = input("Qual o novo nome: ")
            break
        else:
            print("Esse nome nao existe")

    if "idade" in novo_usuario:
        old_age = int(input("qual sua idade atual: "))
        if find(lista, old_age):
            lista[lugar(lista, old_age)] = int(input("Qual sua nova idade: "))
            break
        else:
            print("Essa idade nao existe")
print(lista)
