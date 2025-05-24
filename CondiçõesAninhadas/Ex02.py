"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário  
- 2 para octal  
- 3 para hexadecimal

"""

num = int(input("Entre com um valor decimal: "))

print('''Para qual base deseja converte-lo: 
    [1] para Binario
    [2] para Octal
    [3] para Hexadecimal''')

opcao = int(input("Qual sua opção? "))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else: 
    print("Opção invalida!")

    