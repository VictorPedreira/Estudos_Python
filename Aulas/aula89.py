lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
lista = [
    (x, y) 
    for x in range(3)
    for y in range(3)
]

lista = [
    [(x, y) for y in range(3)]
    for x in range(3)
]

print(lista)