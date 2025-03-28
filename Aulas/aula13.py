nome = str(input("Escreva o seu nome: "))
altura = float(input("Escreva a sua altura em metros: "))
peso = int(input("Escreve o seu peso: "))

imc = peso / (altura ** 2)

"f-strings"
linha_1 = f"{nome} tem {altura:.2f} de altura,"
linha_2 = f"pesa {peso}kg e sua  IMC é de"
linha_3 = f"{imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)