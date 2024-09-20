lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

conjunto1 = set(lista1)
conjunto2 = set(lista2)

print(f'Comuns: {conjunto1.intersection(conjunto2)}')
print(f'Só na primeira: {conjunto1.difference(conjunto2)}')
print(f'Só na segunda: {conjunto2.difference(conjunto1)}')
print(f'Elementos não repetidos: {conjunto1.union(conjunto2)}')
print(f'Lista 1 sem elementos da lista 2: {conjunto1.difference(conjunto2)}')