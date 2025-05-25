#Laço For:

for c in range(0, 6):#incremento de 6
    print(c)
print("End")

for c in range(6, 0, -1):#decremento de 6
    print(c)
print("End")

for c in range(0, 8, 2):#conta de 0 a 8 de 2 em 2
    print(c)
print("End")

print("--------------------------------------------")

n = int(input("Digite um numero: "))
for i in range (0, n+1):
    print(i)
print("End")

print("--------------------------------------------")

inicio = int(input("Inicio: "))
fim  = int(input("Fim: "))
passo = int(input("Passo: "))

for i in range(inicio, fim + 1, passo):
    print(i)
print("End")

print("--------------------------------------------")

s = 0
for i in range(0, 4):
    n = int(input("Digite um numero: "))
    s += n
print("O somantorio de todos os numeros foi {}".format(s))