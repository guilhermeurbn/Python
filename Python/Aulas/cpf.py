#!/usr/bin/env python3
#replicando o seu CPF



cpf_old = input("digite seu CPF: ")

def just_numbers(cpf_old):
    i = 0
    nums = []
    while (i < len(cpf_old)):
        if cpf_old[i].isdigit():
            nums.append(int(cpf_old[i]))
        i += 1
    return nums

def mult_regressiva(nums, mult):
    i = 0
    result = []
    while (i < len(nums)):
        result.append(nums[i] * mult)
        i += 1
        mult -= 1
    return result

def soma_all(lista):
    i = 0
    total = 0
    while (i < len(lista)):
        total += lista[i]
        i += 1
    return total

def new_numbers(soma):
    soma *= 10
    soma %= 11
    if soma > 9:
        return 0
    return soma


cpf = just_numbers(cpf_old)

primeiros_9 = cpf[:9]

tmp1 = mult_regressiva(primeiros_9, 10)
soma_1 = soma_all(tmp1)
dig1 = new_numbers(soma_1)

primeiros_10 = primeiros_9 + [dig1]

tmp2 = mult_regressiva(primeiros_10, 11)
soma_2 = soma_all(tmp2)
dig2 = new_numbers(soma_2)

cpf_new = [dig1, dig2]


print(f"o final do seu codigo é {cpf_new}")
print("Seu CPF é:", cpf)

if cpf[-2:] == cpf_new:
    print("CPF correto")
else:
    print("cpf incorreto")
