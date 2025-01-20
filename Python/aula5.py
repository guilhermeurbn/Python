#calculadora

while True:
    num1 = int(input("digite um numero: "))
    num2 = int(input("digite outro numero: "))
    operador = input("qual operador (+ - / *): ")

    if operador == '+':
        print(f'{num1}{operador}{num2} = {num1 + num2}')
    elif operador == '-':
        print(f'{num1}{operador}{num2} = {num1 - num2}')
    elif operador == '/':
        print(f'{num1} {operador} {num2} = {num1 / num2}')
    elif operador == '*':
        print(f'{num1}{operador}{num2} = {num1 * num2}')

    sair = input("voce deseja sair: ").lower()
    if sair == 'sim' or 's':
        break

print('fim')


