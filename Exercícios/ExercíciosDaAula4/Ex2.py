import random

def jogo_da_forca():
    palavras = ['python', 'programacao', 'desafio', 'computador', 'jogo']
    palavra = random.choice(palavras)
    tentativas = 6
    letras_acertadas = ['_' for _ in palavra]

    while tentativas > 0 and '_' in letras_acertadas:
        print(' '.join(letras_acertadas))
        letra = input('Adivinhe uma letra: ').lower()

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_acertadas[i] = letra
        else:
            tentativas -= 1
            print(f'Letra incorreta! Tentativas restantes: {tentativas}')

    if '_' not in letras_acertadas:
        print(f'Você ganhou! A palavra era: {palavra}')
    else:
        print(f'Você perdeu! A palavra era: {palavra}')

jogo_da_forca()