'''
4. Refação o DESAFIO 009. mostrando a tabuada da um número que o usuário 
escolhar, só que agora utilizando um laço for.

'''
num = int(input("Entre com um numero: "))

for i in range (1, 11):
    result = num * i
    print("{} x {} = {}".format(num, i, result))