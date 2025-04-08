# Exercícios com funções

# Crie uma função que multiplica todos os argumentos 
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
import os

lista = []

def multipliers(*args):
    total = 1
    for numero in args:
        total *= numero
        print(total)
    return total

def impar_par(total):
    if total % 2 == 0:
        return " Par"
    return "Ímpar"
    
while True:
    os.system('cls')
    numeros = input("Digite números: ")
    numeros = int(numeros)

    if numeros == 0:
        print("Zero não é válido, escolha outro número")
        continue

    lista.append(numeros)

    if numeros == 999:
        break
    
lista.pop()

result = multipliers(*lista)

print(f'O resultado da multiplicação é {result} e esse número é {impar_par(result)}')