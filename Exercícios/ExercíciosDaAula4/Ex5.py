V = [9, 8, 7, 12, 0, 13, 21]
pares = [num for num in V if num % 2 == 0]
impares = [num for num in V if num % 2 != 0]

print(f'Pares: {pares}')
print(f'Ímpares: {impares}')