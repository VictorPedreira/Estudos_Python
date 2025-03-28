"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteir, informe que não é um número inteiro.
"""
#-----------------------------------------------------#
num_inteiro = input("Digite um número inteiro: ")

try:
    num_inteiro = int(num_inteiro)
    impar_par = (num_inteiro % 2) == 0
    if impar_par:
        print(f"O número {num_inteiro} é par.")
    else:
        print(f"O númeor {num_inteiro} é ímpar.")   
except:
    print("O número digitado não é um número inteiro")  
#------------------------------------------------------#
"""
Faça um programa que pergunte a hora ao usuário e, 
baseando-se no horário descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
#-----------------------------------------------------#
horario = input("Digite a hora atual (apenas a hora): ")

try:
    horario = int(horario)
    horario_manha = horario >= 0 and horario <= 11
    horario_tarde = horario >= 12 and horario <= 17
    horario_noite = horario >= 18 and horario <=23
    if horario_manha:
        print("Bom dia!")
    elif horario_tarde:
        print("Boa tarde!")
    elif horario_noite:
        print("Boa noite!")
    else:
        print("Horário inválido")
except: 
    print("Esse formato de horário não é aceito") 
#-----------------------------------------------------#              
"""
Faça um programa que peça o primeiro nome de usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
#-----------------------------------------------------#
nome_user = input("Digite o seu primeiro nome: ")
nome_user = str(nome_user)
nome_curto = len(nome_user) <= 4
nome_normal = len(nome_user) >=5 and len(nome_user) <= 6
nome_grande = len(nome_user) > 6

if nome_curto:
    print("Seu nome é curto")
elif nome_normal:
    print("Seu nome é normal")
elif nome_grande:
    print("Seu nome é grande") 
else:
    print("O dado inserido é inválido")   
#-----------------------------------------------------#           
