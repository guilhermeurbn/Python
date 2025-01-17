"""aula numero 54. exercicio"""

#1º exercicio
num = input("digite um numero inteiro: ")
try:
    if (int(num) % 2 == 0):
        print(f"o numero: {num} é Par")
    else:
        print(f"o numero: {num} é Impar")
except ValueError:
    print(f"o numero: {num}, não é um numero inteiro")


#2º exercicio
hora = int(input("senhor me informa as horas: "))
if hora <= 11:
    print("Bom dia senhor!")
elif hora <= 17:
    print("Boa tarde senhor!")
elif hora <= 23:
    print("Boa noite senhor!") 
else:
    print("digite uma hora exata!")


#3º exercicio
nome = input("Qual seu nome: ")

if len(nome) <= 4:
    print("seu nome é Curto")
elif len(nome) <= 6:
    print("seu nome é Normal")
else:
    print("seu nome é muito Grande")
