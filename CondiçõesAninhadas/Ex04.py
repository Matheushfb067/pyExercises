"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de 
acordo com sua idade:  

- Se ele ainda vai se alistar ao serviço militar.  
- Se é a hora de se alistar.  
- Se já passou do tempo do alistamento.  

Seu programa também deverá mostrar o tempo que falta ou que passou do 
prazo.

"""#fazer de acordo com resolução
from datetime import date
ano_atual = date.today().year

nasc = int(input("Entre com o ano de nascimento: "))

idade = ano_atual - nasc
print("Quem nasceu em {} tem {} anos em {}" .format(nasc, idade, ano_atual))

if idade == 18: 
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 19: 
    faltando = 18 - idade
    print("Ainda faltam {} anos para o alistamento!" .format(faltando))
else:
    atraso = idade - 18
    print("Você já deveria ter se alistados a {} anos!".format(atraso))
