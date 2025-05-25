'''
6. Desenvolva um programa que leia o primeiro termo e a razão da uma PA. No final, 
mostre os 10 primeiros termos dessa progressão.

'''
primeiro = int(input("Entre com o primeiro termo: "))
razao = int(input("Entre com a razão: "))

for i in range (10):
    termo = primeiro + i * razao
    print(termo, end=" ")