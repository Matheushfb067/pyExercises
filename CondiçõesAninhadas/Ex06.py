"""
A Confederação Nacional de Natação precisa de um programa que leia o ano 
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM  
- Até 14 anos: INFANTIL  
- Até 19 anos: JÚNIOR  
- Até 20 anos: SÊNIOR  
- Acima: MASTER

"""
from datetime import date
atual = date.today().year

nascimento = int(input("Entre com o ano de nascimento: "))

idade = atual - nascimento
print("O atleta tem {} anos." .format(idade))

if nascimento <= 9: 
    print("MIRIM")
elif nascimento > 9 and nascimento <=14:
    print("INFANTIL")
elif nascimento > 14 and nascimento <= 19:
    print("JÚNIOR") 
elif nascimento > 19 and nascimento <= 20:
    print("SENIOR")
else:
    print("MASTER")