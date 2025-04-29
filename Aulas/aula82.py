# Sets - Conjuntos em Python (tipo set)
# Conjuntos s'ao ensinados na matemática
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor inteiro.

# Criando um set 
# set(iterável) ou {1, 2, 3}
s1 = set('Luiz')
s1 = set() # vazio
s1 = {'Luiz', 1, 2, 3} # com dados

# Sets são eficientes para remover valores duplicados 
# de iteráveis.
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not inw)
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
s1 = {1, 2, 3}
print(3 not in s1)
for numero in s1:
  print(numero)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4))
s1.clear()
s1.discard('Luiz')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecções & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda 
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)