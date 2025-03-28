nome = str(input("Escreva o seu nome: "))
altura = float(input("Escreva a sua altura em metros: "))
peso = int(input("Escreve o seu peso: "))

imc = peso / (altura ** 2)
print(f"Seu nome é {nome}, sua altura é {altura} metros, seu peso é de {peso}kg,e o seu imc eh igual a {imc:.2f}")
