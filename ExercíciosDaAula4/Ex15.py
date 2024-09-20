agenda = {}

def menu():
    print("1. Adicionar entrada")
    print("2. Alterar entrada")
    print("3. Listar entradas")
    print("4. Apagar entrada")
    print("5. Sair")

def adicionar():
    nome = input("Nome: ")
    if nome in agenda:
        print("Nome já existe.")
    else:
        idade = input("Idade: ")