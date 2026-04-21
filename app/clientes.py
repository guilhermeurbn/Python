import json

clientes = []

def carregar_dados():
    try:
        with open("clientes.json", "r") as arquivos:
            return json.load(arquivos)
    except:
         return []

def salvar_dados(clientes):
     with open("clientes.json", "w") as arquivo:
          json.dump(clientes, arquivo, indent=4)

def registrar_cliente():
    cliente = {
        "nome" : input("Nome: ").upper(),
        "idade" : int(input("idade: ")),
        "sexo" : input("Sexo: ").upper()
    }
    return (cliente)
#serve para mim retornar a posição do cliente
def find_cliente(buscar_cliente, clientes):
    i = 0
    while i < len(clientes):
        if clientes[i]['nome'] == buscar_cliente.upper():
            return (clientes[i])
        i+= 1
    return (None)

def find_cliente_atualizar(buscar_cliente, clientes):
    i = 0
    while i < len(clientes):
        if clientes[i]['nome'] == buscar_cliente.upper():
            clientes[i] = registrar_cliente()
        i+= 1
    salvar_dados(clientes)
    return (True)

def find_delete(buscar_cliente, clientes):
    i = 0
    encontrado = False
    while i < len(clientes):
        if clientes[i]['nome'] == buscar_cliente.upper():
            del clientes[i]
            encontrado = True
            break
        i+=1
    
    if encontrado:
        print("Deletado com sucesso")
        salvar_dados(clientes)
    else:
        print("Cliente não encontrado")