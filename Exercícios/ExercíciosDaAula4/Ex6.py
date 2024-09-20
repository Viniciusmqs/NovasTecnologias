lugares_vagos = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Digite o número da sala (0 para sair): "))
    if sala == 0:
        break
    lugares_solicitados = int(input("Quantos lugares deseja solicitar? "))

    if sala >= 1 and sala <= 5:
        if lugares_vagos[sala - 1] >= lugares_solicitados:
            lugares_vagos[sala - 1] -= lugares_solicitados
            print(f'Vendido! Lugares restantes na sala {sala}: {lugares_vagos[sala - 1]}')
        else:
            print(f'Não há lugares suficientes na sala {sala}.')
    else:
        print('Sala inválida.')