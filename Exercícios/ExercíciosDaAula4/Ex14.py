def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(' | '.join(linha))
        print('-' * 5)

def jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogadores = ['X', 'O']
    vencedor = None

    for jogada in range(9):
        jogador_atual = jogadores[jogada % 2]
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f'Jogador {jogador_atual}, escolha a linha (0-2): '))
        coluna = int(input(f'Jogador {jogador_atual}, escolha a coluna (0-2): '))

        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador_atual
            # Verificar vitória
            if any(all(tabuleiro[i][j] == jogador_atual for j in range(3)) for i in range(3)) or \
               any(all(tabuleiro[j][i] == jogador_atual for j in range(3)) for i in range(3)) or \
               all(tabuleiro[i][i] == jogador_atual for i in range(3)) or \
               all(tabuleiro[i][2 - i] == jogador_atual for i in range(3)):
                vencedor = jogador_atual
                break
        else:
            print('Posição já ocupada, tente novamente.')
            jogada -= 1

    exibir_tabuleiro(tabuleiro)
    if vencedor:
        print(f'Jogador {vencedor} venceu!')
    else:
        print('Empate!')

jogo_da_velha()