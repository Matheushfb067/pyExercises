"""
Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO  
- Média entre 5.0 e 6.9: RECUPERAÇÃO  
- Média 7.0 ou superior: APROVADO

"""

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))

media = (nota1 + nota2) / 2
print("Se o aluno tirou {:.1f} e {:.1f}, a media do aluno é {:.1f}" .format(nota1, nota2, media))

if media < 5: 
    print("REPROVADO!")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO!")
else: 
    print("APROVADO!")