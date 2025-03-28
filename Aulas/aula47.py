"""
Faça um jogo para o usuário adivinhar qual a palavra secreta;
- Você vai propor um palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na 
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver 
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.    
"""

# Minha resolução
# print(10*'=',"Bem vindo ao jogo da palavra S-E-C-R-E-T-A",10*'=')
# print("")
# palavra_secreta = 'Perfume'.lower()
# palavra_oculta = '*' * len(palavra_secreta)
# tentativas = 0

# while palavra_oculta != palavra_secreta:
#     print('-'*30)
#     letra = input('Digite uma letra: ').lower()

#     if len(letra) != 1 or not letra_digitada.isalpha():
#         letra = input('Digite apenas uma letra: ').lower()
#     elif letra in palavra_secreta:
#         print('Maravilha, você encontrou um letra que está na palavra!!!!')
#     else: 
#         print('Que pena, você não encontrou a letra que você procurava!!!!')
#     nova_palavra_oculta = ''
#     for i in range(len(palavra_secreta)):
#         if letra == palavra_secreta[i] or palavra_oculta[i] != '*':
#             nova_palavra_oculta += palavra_secreta[i]
#         else: 
#             nova_palavra_oculta += '*'
#     palavra_oculta = nova_palavra_oculta 
#     tentativas += 1

#     print(f'A palavra secreta é = {nova_palavra_oculta}')   

# print('Parabens!!!!! Você completou a palavra secreta')
# print(f'Você finalizou o jogo em {tentativas} tentativas') 

#Resolução do professor 1
# import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas UMA LETRA!! ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada


    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        # os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS')       
        print('Palavra secreta: ', palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0


