
def zenit_polar(texto, modo='criptografar'):
    # Mapeamento das letras (minúsculas e maiúsculas)
    mapa_cripto = {
        'z': 'p', 'p': 'z',
        'e': 'o', 'o': 'e',
        'n': 'l', 'l': 'n',
        'i': 'a', 'a': 'i',
        't': 'r', 'r': 't',
        'Z': 'P', 'P': 'Z',
        'E': 'O', 'O': 'E',
        'N': 'L', 'L': 'N',
        'I': 'A', 'A': 'I',
        'T': 'R', 'R': 'T'
    }

    resultado = []
    for caractere in text:
        if caractere in mapa_cripto:
            # Substitui o caractere conforme o mapa
            novo_caractere = mapa_cripto[caractere]
            resultado.append(novo_caractere)
        else:
            # Mantém o caractere se não estiver no mapa
            resultado.append(caractere)
    
    return ''.join(resultado)

# Exemplo de uso:
texto_original = "Zenit Polar"
texto_criptografado = zenit_polar(texto_original)
print("Criptografado:", texto_criptografado)  # Saída: "Ponat Leraz"

texto_descriptografado = zenit_polar(texto_criptografado)
print("Descriptografado:", texto_descriptografado)  # Saída: "Zenit Polar"