# Encripitar usando ZENIT POLAR
# Uso de letras, números e caracteres especiais

def zenit_polar(texto):
    # Mapa de substituição para LETRAS (Zenit Polar)
    substituicoes_letras = {
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

    # Mapa de substituição para NÚMEROS (0-4 ↔ 5-9)
    substituicoes_numeros = {
        '0': '5', '5': '0',
        '1': '6', '6': '1',
        '2': '7', '7': '2',
        '3': '8', '8': '3',
        '4': '9', '9': '4'
    }

    # Mapa de substituição para CARACTERES ESPECIAIS (personalizável)
    substituicoes_especiais = {
        '@': '#', '#': '@',
        '!': '?', '?': '!',
        '$': '&', '&': '$',
        '%': '*', '*': '%'
    }

    resultado = []
    for caractere in texto:
        # Verifica se é uma letra para substituir
        if caractere in substituicoes_letras:
            resultado.append(substituicoes_letras[caractere])
        # Verifica se é um número para substituir
        elif caractere in substituicoes_numeros:
            resultado.append(substituicoes_numeros[caractere])
        # Verifica se é um caractere especial para substituir
        elif caractere in substituicoes_especiais:
            resultado.append(substituicoes_especiais[caractere])
        # Mantém o caractere se não estiver em nenhum mapa
        else:
            resultado.append(caractere)
    return ''.join(resultado)

def main():
    print("\n--- Cifra Zenit Polar (Letras + Números + Caracteres Especiais) ---")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Sair")

    while True:
        opcao = input("\nEscolha uma opção (1/2/3): ").strip()

        if opcao == '1':
            palavra = input("Digite o texto para ENCRIPTAR: ")
            encriptado = zenit_polar(palavra)
            print(f"Resultado: {encriptado}")

        elif opcao == '2':
            palavra = input("Digite o texto para DESENCRIPTAR: ")
            desencriptado = zenit_polar(palavra)  # A função é a mesma!
            print(f"Resultado: {desencriptado}")

        elif opcao == '3':
            print("Saindo... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()