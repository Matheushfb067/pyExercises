'''
7. Faça um programa que leia um número inteiro e diga se ela é ou não um 
número primo.

'''
num = int(input("Entre com um numero: "))
div = 0 #quantidade de divisões que o nummero pode ter
for i in range (1, num+1):
    if num % i == 0:
        print('\033[33m', end=" ")#manipulação de cores
        div += 1
    else:
        print('\033[31m', end=" ")#manipulação de cores
    print('{}'.format(i), end=" ")
print('\n\033[mO numero {} foi dividido {} vezes'.format(num, div))

#verificação se tem apenas 2 divisores
if div == 2:
    print("É Primo!")
else:
    print("Não é Primo!")