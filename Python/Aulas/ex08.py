#!/usr/bin/env python3

"""Faca uma lista de comprar com listas
pode inserir, listar ou apagar
🎯 Objetivo

Construir um sistema onde o usuário pode:
	•	Adicionar tarefas
	•	Listar tarefas
	•	Marcar como concluída
	•	Remover tarefa
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Remover tarefa
0 - Sair
nao pode quebrar com indices inexistentes"""



lista = []

while(1):
    print("1 - Adicionar tarefa\n")
    print("2 - Listar tarefa   \n")
    print("3 - Concluir tarefa \n")
    print("4 - Remover tarefa  \n")
    print("0 - Sair            \n")
    usuario = input("Qual opção deseja:").lstrip()

    if "1" == usuario:
        lista.append(input("Adicionar: "))

    elif "2" == usuario:
        if len(lista) == 0:
            print("\nNão existe o que ser Listado\n")
            continue
        
        for i, a in enumerate(lista):
            print(f"\n [{i}] {a}")
        print("\n")
    
    elif "3" == usuario:
        if len(lista) == 0:
            print("\nNada para concluir\n")
            continue

        for i, a in enumerate(lista):
            print(f"\n [{i}] {a}")

        while True:
            opcao = input("\nQual da lista voce deseja concluir: ")

            if not opcao.isdigit():
                print("\nDigite um número válido\n")
                continue

            opcao = int(opcao)

            if opcao < 0 or opcao >= len(lista):
                print(f"\nDigite entre 0 e {len(lista) - 1}\n")
                continue

            break
        if "✅" not in lista[opcao]:
            lista[opcao] += " ✅"

        print(f"\n[x] {lista[opcao]}\n")

    elif "4" == usuario:
        if len(lista) == 0:
            print("Não existe o que ser apagado\n")
            continue

        for i, a in enumerate(lista):
            print(f"[{i}] {a}")

        indice = input("Qual tarefa gostaria de apagar: \n")

        if not indice.isdigit():
            print("Digite um número válido\n")
            continue

        indice = int(indice)

        if indice < 0 or indice >= len(lista):
            print("Indice inexistente\n")
            continue

        print(f"[x] {lista[indice]}\n")
        lista.pop(indice)

    elif '0' == usuario:
        break
    else:
        print("Por favor escolha [1][2][3][4][0]\n")