'''
Faça um programa que mostra na tela uma contagem regressiva para o estouro 
da fogos de artificio. Indo da 10 até 0, com uma pausa de 1 segundo antre eles.

'''
import time

for i in range (10, 0, -1):
    print(i)
    time.sleep(1)
print("BUM! Fogos de Artificio!")
