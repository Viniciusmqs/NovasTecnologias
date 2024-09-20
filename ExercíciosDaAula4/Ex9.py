versao_inicial = [1, 2, 3, 4]
versao_alterada = [3, 4, 5, 6]

inicial_set = set(versao_inicial)
alterada_set = set(versao_alterada)

print(f'Elementos que não mudaram: {inicial_set.intersection(alterada_set)}')
print(f'Novos elementos: {alterada_set.difference(inicial_set)}')
print(f'Elementos removidos: {inicial_set.difference(alterada_set)}')