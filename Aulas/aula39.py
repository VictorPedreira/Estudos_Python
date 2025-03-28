"""
Iterando strings com while
"""
#       012345678910
nome = "Victor Pedreira" # Iteráveis
#      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])
contador = 0
novo_nome = ''

while contador < len(nome):
    letra = nome[contador]
    novo_nome += '*'
    novo_nome += letra
    contador += 1

novo_nome += '*'
print(novo_nome) 
  

