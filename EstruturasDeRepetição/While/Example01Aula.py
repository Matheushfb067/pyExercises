#Exemplo de Aula
#while: estrutura de repetição com teste lógico!
 
'''
for i in range(1, 10):
    print(i)
print("End")
'''
#mesma coisa do exemplo acima com o for, usando a estrutura while
#while serve quando o limite é dado ou não,já o for depende de um limite

c = 1
while c < 10:
    print(c)
    c += 1
print("End")

#--------------------------------------------------------------------------#
''' #lê 4 entradas de dados de forma limitada
for i in range (1, 5):
    n = int(input("Digite um valor: "))
print("Fim")
'''
#mesma coisa do exemplo acima quebrando o loop se a entrada for igual a 0.
#flag = 0 - roda infinitas vezes a menos q 0 seja digitado.

n = 1
while n != 0:
    n = int(input("Entre com um numero: "))
print("Fim")

#--------------------------------------------------------------------------#
#Continua a entrada de dados a menos que seja digitado algo diferente de S

r = 'S'
while r == 'S':
    n = int(input("Entre com um numero: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("Fim")

#--------------------------------------------------------------------------#
#contador impar/par:
n = 1
par = 0
impar = 0

while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0: #teste só roda se n for diferente de 0, 0 não é par ou impar
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Acabou")

print("Quantidade de numeros pares {} ".format(par))
print("Quantidade de numeros impares {} ".format(impar))