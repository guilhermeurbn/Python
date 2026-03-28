#!/usr/bin/env python3
"""Faca uma lista de comprar com listas
pode inserir, listar ou apagar
nao pode quebrar com indices inexistentes"""



lista = []

while(1):
    print(len(lista))
    print("Lista de compras I(nserir) A(pagar) L(istar)")
    usuario = input("Qual opção deseja: ").lstrip()

    if "i" in usuario:
        lista.append(input("inserir: "))

    elif "a" in usuario:
        if len(lista) == 0:
            print("Não existe o que ser apagado")
            continue

        indice = int(input("qual indice gostaria de apagar: "))
        if (indice >= len(lista) or indice < 0):
            print("Indice inexistente")
            continue

        lista.pop(indice)
        print("indice Apagado")

    elif "l" in usuario:
        if len(lista) == 0:
            print("Não existe o que ser Listado")
            continue

        for i, a in enumerate(lista):
            print(i, a)
    
    else:
        print("Por favor escolha [i][a][l]")



        