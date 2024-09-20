def verificar_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha or pilha[-1] != '(':
                return "Erro"
            pilha.pop()

    return "OK" if not pilha else "Erro"

# Exemplos de uso
print(verificar_parenteses("(())"))       # OK
print(verificar_parenteses("()()(()())"))  # OK
print(verificar_parenteses("(()"))         # Erro
print(verificar_parenteses("( ) )"))       # Erro