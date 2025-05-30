'''
8. Crie um programa que leia uma frase qualquer e diga se ela é um 
palindromo, desconsiderando os espaços.

Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA

'''
#strip(): desconsidera os espaços 
#uper(): passa para maiusculo
#split(): divide a frase por palavras
#join(): junta as palavras sem nenhum espaço
#len(): pega o tamanho da string

frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto: 
    print("Temos um palindromo!")
else:
    print("Não é um palindromo")