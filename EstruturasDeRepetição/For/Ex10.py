'''
10. Faça um programa que leia o peso de cinco pessoas. No final, mostre 
quais foram o maior e o menor peso lidos.

'''
ma = 0
me = 0

for i in range(5):
    peso = float(input("Entre com o peso: "))

    if i == 0: #faz com que o primeiro valor digitado seja armazenado em ma e me, para que a iteração ocorra corretamente!
        ma = peso 
        me = peso
    else: 
        if peso > ma:
            ma = peso
        if peso < me:
            me = peso
print("O maior peso lido foi: {:.2f}kg ".format(ma))
print("O menor peso lido foi: {:.2f}kg ".format(me))