"""
Refaça o DESAFIO dos triângulos, acrescentando o recurso de mostrar que 
tipo de triângulo será formado:

- Equilátero: todos os lados iguais  
- Isósceles: dois lados iguais  
- Escaleno: todos os lados diferentes

Desafio dos triangulos: Dasenvolva um programa que leia o comprimento de 
três retas e diga ao usuário se elas podem ou não formar um triângulo."

"""
print("-"*30)
print("Analizador de Triangulos")
print("-"*30)

l1 = float(input("Primeiro Segmento: "))
l2 = float(input("Segundo Segmento: "))
l3 = float(input("Terceiro Segmento: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segumento PODEM formar um triangulo ", end='')
    
    if l1 == l2 == l3: #o python permite fazer a igualdade entre todos elementos
        print("EQULÁTERO")
    elif l1 != l2 != l3 != l1: #o python permite fazer a desigualdade entre todos elementos
        print("ESCALENO")
    else:
        print("ISÓCELES")

else:
    print("Os segumento NÃO PODEM formar um triangulo")



