'''
5. Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daquelas que forem pares. Se o valor digitado for ímpar, desconsidere-o.

'''
soma = 0
for i in range(6):
    num = int(input("Entre com um numero: "))
    if num % 2 == 0:
        soma += num
print("A soma dos pares é: {}".format(soma))