lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

maior = max(lista)
print(f'Maior elemento: {maior}')

menor = min(lista) 
print(f'Menor elemento: {menor}')

pares = [num for num in lista if num % 2 == 0]
print(f'Par elemento: {pares}')

ocorrencias_primeiro = lista.count(lista[0])
print(f'O numero de ocorrencias do primeiro elemento ({lista[0]}): {ocorrencias_primeiro}')

media = sum(lista) / len(lista)
print(f'Média dos elementos: {media:2f}')

soma_negativos = sum(num for num in lista if num < 0)
print(f'soma dos elementos negativos: {soma_negativos}')

