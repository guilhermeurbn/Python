#!/usr/bin/env python3
#replicando o seu CPF

i = 0
cpf_tmp = []
cpf_old = input("digite seu CPF: ")
cpf = []
# 1ª Parte: Separando apenas os numeros
while(i < len(cpf_old)):
    if not cpf_old[i].isdigit():
        i += 1
        continue
    cpf.append(int(cpf_old[i]))
    i += 1
                                    #012.345.678-99
print(cpf)

#2ªParte: multiplicar numa ordem regressiva do 10

i = 0
j = 10
while(i < len(cpf)):
    cpf_tmp.append(cpf[i] * j)
    i += 1
    j -= 1

#3ªParte: Somar todos os valores
i = 0
cpf_soma = 0
while (i < len(cpf)):                 #746824890
    cpf_soma += cpf_tmp[i]
    i += 1

#4ªParte: Multiplicar o resultado anterior por 10

cpf_soma *= 10

cpf_soma %= 11

if cpf_soma > 9:
    cpf.append(0)

else:
    cpf.append(cpf_soma)

#Segundo digito

cpf_tmp = []
i = 0
j = 11
while(i < len(cpf)):
    cpf_tmp.append(cpf[i] * j)
    i += 1
    j -= 1

#3ªParte: Somar todos os valores
i = 0
cpf_soma = 0
while (i < len(cpf)):                 #746824890
    cpf_soma += cpf_tmp[i]
    i += 1

#4ªParte: multiplicar por 10
cpf_soma *= 10
cpf_soma %= 11

if cpf_soma > 9:
    cpf.append(0)

else:
    cpf.append(cpf_soma)
print(cpf)
