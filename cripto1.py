# Encripitar usando ZENIT POLAR
# Uso de LETRAS

def zenit_polar(texto):
    # Mapa de substituição (Zenit Polar)
    substituicoes = {
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
    for letra in texto:
        resultado.append(substituicoes.get(letra, letra))  # Substitui ou mantém se não existir no mapa
    return ''.join(resultado)

def main():
    print("\n--- Cifra Zenit Polar ---")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Sair")

    while True:
        opcao = input("\nEscolha uma opção (1/2/3): ").strip()

        if opcao == '1':
            palavra = input("Digite a palavra para ENCRIPTAR: ")
            encriptada = zenit_polar(palavra)
            print(f"Resultado: {encriptada}")

        elif opcao == '2':
            palavra = input("Digite a palavra para DESENCRIPTAR: ")
            desencriptada = zenit_polar(palavra)  # A função é a mesma para descriptar!
            print(f"Resultado: {desencriptada}")

        elif opcao == '3':
            print("Saindo... Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()