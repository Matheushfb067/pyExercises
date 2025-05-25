'''
11. Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo.

Qual é o nome do homem mais velho.

Quantas mulheres têm menos de 20 anos.

'''

soma = 0
h_maisvelho = ''
idade_mais_velho = 0
mulheres = 0

for i in range(4):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ")).strip().upper()

    soma += idade

    if sexo == "M":
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            h_maisvelho = nome
    elif sexo == "F":
        if idade < 20:
            mulheres += 1

media = soma / 4

print("A média das idade é: {} anos.".format(media))
print("O nome do homem mais velho é: {}".format(h_maisvelho))
print("A quantidade de mulheres que tem meno de 20 anos é: {}".format(mulheres))