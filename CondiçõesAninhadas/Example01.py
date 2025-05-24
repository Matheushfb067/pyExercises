nome = str(input('Qual e seu nome? '))
#Estrutura condicional simples: 
if nome == "Matheus":
    print("Que nome Bonito!")
#Estrutura condicional aninhada:
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome é bem popular no Brasil!")
elif nome in ['Ana', 'Claudia', 'Jesica', 'Juliana']:
    print("Belo nome")
#Estrutura condicional composta:
else: 
    print("Seu nome é bem normal!")
print("Tenha um Bom dia! {}".format(nome))