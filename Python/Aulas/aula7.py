#aula 07

lista = []

cores = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "reset": "\033[0m"
}

def color(texto, cor):
    if cor in cores:
        return cores[cor] + texto + cores["reset"]
    return texto


def find(lista, old_name):
    i = 0
    while i < len(lista):
        if lista[i] == old_name:
            return True
        i += 1
    return (False)

def lugar(lista, old_name):
    i = 0
    while i < len(lista):
        if lista[i] == old_name:
            return i
        i += 1

i = 0
usuario = " "

while(usuario != "exit"):

    usuario = input("\nO que voce gostaria de fazer\n \n\tMudar nome: \n"\
                    "\tAdicionar nome:\n\tRemover nome:\n\tlista nomes:\n :")
    
    if "mudar" in usuario:
        old_name = input("qual seu nome atual: ")
        if find(lista, old_name):
            lista[lugar(lista, old_name)] = str(input("Qual o novo nome: ")).lstrip().rstrip()
            print(color(lista[-1], "blue"))
        else:
            print(color("\n\tNOT EXISTED NAME", "red"))

    elif "adicionar" in usuario:
        new_name = str(input("Qual vai ser o nome adicionado: ")).lstrip().rstrip()
        lista.append(new_name)
        print(color(lista[-1], "blue"))
        print(color("NEW NAME", "blue"))
        
    elif "remover" in usuario:
        rem_name = input("Qual nome pra remover: ").lstrip().rstrip()
        if find(lista, rem_name):
            lista.pop()
            print(color("NOME DELETADO", "red"))
    elif "lista" in usuario:
        print(lista)
        
print(lista)
