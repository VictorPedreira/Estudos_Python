""" Calculadora com while"""


while True:
    numero_1 = input("Digite o primeiro numero: ")
    numero_2 = input("Digite o segundo numero: ")
    operador = input("Digite a operação desejada (+-*/): ")
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números digitados são inválidos.")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador Invalido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        print(f'O resultado da soma entre {numero_1_float} e {numero_2_float} é {numero_1_float + numero_2_float}')
    elif operador == '-':
        print(f'O resultado a subtração entre {numero_1_float} e {numero_2_float} é {numero_1_float - numero_2_float}')
    elif operador == '*':
        print(f'O resultado a multiplicação entre {numero_1_float} e {numero_2_float} é {numero_1_float * numero_2_float}')
    elif operador == '/':
        print(f'O resultado a divisão entre {numero_1_float} e {numero_2_float} é {numero_1_float // numero_2_float}')
    else:
        print("Você não deveria conseguri chegar até aqui")
        

    sair = input("Caso deseje sair digite [S]air ou se quiser continuar [F]icar e pressione enter: ").lower().startswith('s')
    if sair is True:
        break
    else:
        continue

print("Você saiu da Calculadora ")