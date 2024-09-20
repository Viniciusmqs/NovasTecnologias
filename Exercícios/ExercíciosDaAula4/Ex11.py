pessoa1 = {'first_name': 'Vinícius', 'last_name': 'Marques', 'age': 30, 'city': 'São Paulo'}
pessoa2 = {'first_name': 'Ana', 'last_name': 'Silva', 'age': 25, 'city': 'Rio de Janeiro'}
pessoa3 = {'first_name': 'Carlos', 'last_name': 'Pereira', 'age': 28, 'city': 'Belo Horizonte'}

people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    for chave, valor in pessoa.items():
        print(f'{chave}: {valor}')
    print()