# Manipulando chaves de valores em dicionários
pessoa = {}  

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome', None))
if pessoa.get('sobrenome', None) is None:
    print('NÃO EXISTE')
else:   
    print(pessoa['sobrenome'])
# print('ISSO Não vai')
