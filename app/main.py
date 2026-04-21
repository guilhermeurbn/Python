#!/usr/bin/env python3
from clientes import (
    carregar_dados,
    salvar_dados,
    registrar_cliente,
    find_cliente,
    find_cliente_atualizar,
    find_delete,     )

clientes = carregar_dados()


while(True):    

    #perguntar o que deseja, CRUD (criar, read, update, delete)
    print("\n1: Lista de Clientes".upper())
    print("2: Acrescentar Cliente".upper())
    print("3: Atualizar Clientes".upper())
    print("4: Deletar Clientes".upper())
    print("5: Buscar Clientes".upper())
    print("0: Sair".upper())
    while (True):
        try:
            usuario = int(input(":"))
            break
        except:
            print("Digite um numero: \n")
    #listar
    if usuario == 1:

        if len(clientes) == 0:
            print("Lista vazia\n".upper())
        else:
            i = 0
            for cliente in clientes:
                print(f"Nome: {clientes[i]['nome']}")
                print(f"Idade: {clientes[i]['idade']}")
                print(f"Sexo: {clientes[i]['sexo']}\n")
                i+=1
    #acrescentar
    if usuario == 2:
        numeros_clientes = int(input("\nQuantos clientes para se registrar: "))
        for _ in range(0, numeros_clientes):
            cliente = registrar_cliente()
            clientes.append(cliente)
        salvar_dados(clientes)
    #atualizar
    if usuario == 3:
        buscar_cliente = input("\nQual o nome do cliente: ")
        resultado = find_cliente(buscar_cliente, clientes)
        
        if resultado:
            print("\nCliente encontrado\n")
            print(f"Nome: {resultado['nome']}")
            print(f"Idade: {resultado['idade']}")
            print(f"Sexo: {resultado['sexo']}\n")
        else:
            print("Cliente não encontrado")
        
        find_cliente_atualizar(buscar_cliente, clientes)
        print("vamos atualizar")

    
    if usuario == 4:
        if len(clientes) == 0:
            print("Lista vazia\n".upper())
            continue
        buscar_cliente = input("Qual o nome do cliente: ")
        resultado = find_cliente(buscar_cliente, clientes)
        if resultado:
            print("\nCliente encontrado\n")
            print(f"Nome: {resultado['nome']}")
            print(f"Idade: {resultado['idade']}")
            print(f"Sexo: {resultado['sexo']}\n")
        
            find_delete(buscar_cliente, clientes)
            print("Lista atualizada".upper())
        else:
            print("Cliente não encontrado")

    if usuario == 5:
        buscar_cliente = input("Qual o nome do cliente: ")
        resultado = find_cliente(buscar_cliente, clientes)
        
        if resultado:
            print("\nCliente encontrado\n")
            print(f"Nome: {resultado['nome']}")
            print(f"Idade: {resultado['idade']}")
            print(f"Sexo: {resultado['sexo']}\n")
        else:
            print("Cliente não encontrado")

    if usuario == 0:
        break
