"""exercicio"""

import random
import os

banco_de_dados = ["guilherme", "neymar", "lasanha", "milena"]
palavra_secreta = random.choice(banco_de_dados)
letras_acertadas = ''
formatada = ''
numeros_tentativas = 0

while True:
    letra = input("digite uma letra: ")
    numeros_tentativas += 1

    if len(letra) > 1:
        print("digite uma letra")
        continue
    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print("palavra formada:", palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print("VOCE GANHOU!!")
        print("numero de tentativas:", numeros_tentativas)
        letras_acertadas = ''
        numeros_tentativas = 0
        break
