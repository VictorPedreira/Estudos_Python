"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

lista_compras = []
letras_aceitas = 'i, a, l'

while True:

    opcoes = input("Selecione uma opção abaixo\n[i]nserir [a]pagar [l]istar: ").lower()
    if opcoes in letras_aceitas:
        if opcoes == 'i':
            os.system('cls')
            item = input("Isira o item que deseja adiconar a lista: ")
            lista_compras.append(item)
        elif opcoes == 'a':
            try:
                os.system('cls')
                apagar = int(input("Digite o número correspondete ao item que deseja apagar: "))
                lista_compras.pop(apagar)
            except:
                os.system('cls')
                print("Você digitou um numero invalido, tente novamente!")
        elif opcoes == 'l':
            os.system('cls')
            if len(lista_compras) == 0:
                print("Sua lista está vazia!")
            elif len(lista_compras) >= 1:
                print("A lista de comprar possui os seguintes itens: ")
                for i in lista_compras:
                    print(lista_compras.index(i), i)
                    
        
    elif opcoes not in letras_aceitas:
        os.system('cls')
        print("ERRO: Opções invalidas, tente novamente!")

#Resolução do professor
# import os

# lista = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         os. system('clear')
#         valor = input('Valor: ')
#         lista.append(valor)
#     elif opcao == 'a':
#         try:
#             indice_str = input('Escolha o índice para apagar: ')
#             indice = int(indice_str)
#             del lista[indice]
#         except ValueError:
#             print('Por favor digite um número inteiro.') 
#         except IndexError:
#             print('Índice não existe na lista') 
#         except Exception:
#             print('Erro desconhecido')
#     elif opcao == 'l':
#         os.system('clear')

#         if len(lista) == 0:
#             print('Nada para listar')

#         for i, valor in enumerate(lista):
#             print(i, valor)

#     else:
#         print('Por favor, escolha i, a ou l.')
