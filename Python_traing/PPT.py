"""pedra pepel ou tesoura"""

import random
import time

print('-' * 34)
print("VAMOS JOGAR PEDRA PAPEL OU TESOURA")
print('-' * 34)

jogos = 0
perdeu = 0
vitoria = 0
empate = 0
while (True):
    enter = input("gostaria de jogar = s[im] / n[ão]: ").lower()
    if enter == "sim":
        num = random.choice(["papel", "pedra", "tesoura"])
        escolha = input("escolha [PEDRA] [PAPEL] [TESOURA]: ").lower()
        jogos += 1
        if num == escolha:
            print(f"{num} x {escolha} = empate")
            empate += 1
        elif num == "pedra" and escolha == "tesoura":
            print(f"{num} x {escolha} = você Perdeu!")
            perdeu += 1
        elif num == "pedra" and escolha == "papel":
            print(f"{num} x {escolha} = você Ganhou!")
            vitoria += 1
        elif num == "papel" and escolha == "pedra":
            print(f"{num} x {escolha} = você Perdeu!")
            perdeu += 1
        elif num == "papel" and escolha == "tesoura":
            print(f"{num} x {escolha} = você Ganhou!")
            vitoria += 1
        elif num == "tesoura" and escolha == "papel":
            print(f"{num} x {escolha} = você Perdeu!")
            perdeu += 1
        elif num == "tesoura" and escolha == "pedra":
            print(f"{num} x {escolha} = você Ganhou!")
            vitoria += 1
    else:
        break
print('-' * 20)
print("FIM DE JOGO")
print('-' * 20)

print('\n')
print("----VAMOS VER SEUS RESULTADOS!----\n")
time.sleep(2)

print(f"você Jogou: {jogos}x")
print(f"você Ganhou: {vitoria}x")
print(f"você Perdeu: {perdeu}x")
print(f"você Empatou: {empate}x")


            

