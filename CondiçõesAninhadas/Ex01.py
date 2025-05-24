"""
Escreva um programa para aprovar o empréstimo bancário para a compra de 
uma casa. O programa vai perguntar o valor da casa, o salário do comprador 
e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% 
do salário ou então o empréstimo será negado.

"""

valor = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o seu salario? R$ "))
anos = int(input("Em quantos anos será paga? R$ "))

#calcula o numero de meses e a quantidade de prestações:
meses = anos * 12
prestacao = valor / meses

max_prestacao = salario * 0.30

print(f"Para comprar uma casa de R$ {valor:.2f} em {anos} anos")
print(f"A prestação será de R$ {prestacao:.2f}")

if prestacao <= max_prestacao:
    print("Emprestimo Aprovado!")
else:
    print("Emprestimo Negado!")