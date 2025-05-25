'''
9. Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''
from datetime import date
ano_atual = date.today().year

#inicializadores:
menores = 0
maiores = 0

for i in range(7):
    ano = int(input("Entre com o ano de nascimento: "))
    idade = ano_atual - ano
    if idade < 18:
        menores += 1
    else: 
        maiores += 1

print("{} pessoas ainda não atingiram a maioridade".format(menores))
print("{} pessoas ainda já atingiram a maioridade".format(maiores))

