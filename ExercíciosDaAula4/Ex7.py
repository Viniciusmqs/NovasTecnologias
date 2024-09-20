frase = input("Digite uma frase: ")
dicionario = {}

for char in frase:
    dicionario[char] = dicionario.get(char, 0) + 1

print(dicionario)