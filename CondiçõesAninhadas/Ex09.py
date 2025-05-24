"""
Crie um programa que faça o computador jogar JoKenPo com você:

"""
import random 
import time

random.seed(time.time())

print('---------------------------JoKenPo---------------------------')

player = int(input('''Entre com um numero de 1 a 3: "
    [1] para PEDRA
    [2] para PAPEL
    [3] para TESOURA \n'''))
print('-------------------------------------------------------------')

if player == 1: 
    print("O jogador escolheu PEDRA")
elif player == 2: 
    print("O jogador escolheu PAPEL")
elif player == 3: 
    print("O jogador escolheu TESOURA")
else:
    print("Opção invalida")
    exit()

computador = random.randint(1, 3)

if computador == 1: 
    print("O computador escolheu PEDRA")
elif computador == 2: 
    print("O computador escolheu PAPEL")
elif computador == 3: 
    print("O computador escolheu TESOURA")
else:
    print("Opção invalida")
    exit()

print('-------------------------------------------------------------')
2
if player == computador: 
    print("Empate!")
elif (player == 1 and computador ==  3) or (player == 2 and computador == 1) or (player == 3 and computador == 2):
    print("O Jogador Ganhou!")
else: 
    print("O Computador Ganhou!")
