# Exercícios
# Crie funções que duplicam, triplicam e quadriplicam
# 0 número recebido como parâmetro.

def criar_contas(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar = criar_contas(2)
triplicar = criar_contas(3)
quadruplicar = criar_contas(4)
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))



# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))