# Criptografia usando zenit-polar

import PySimpleGUI as sg

def zenit_polar(texto):
    substituicoes = {
        # Letras (Zenit Polar)
        'z': 'p', 'p': 'z', 'e': 'o', 'o': 'e', 'n': 'l', 'l': 'n',
        'i': 'a', 'a': 'i', 't': 'r', 'r': 't',
        'Z': 'P', 'P': 'Z', 'E': 'O', 'O': 'E', 'N': 'L', 'L': 'N',
        'I': 'A', 'A': 'I', 'T': 'R', 'R': 'T',
        # Números (0-4 ↔ 5-9)
        '0': '5', '5': '0', '1': '6', '6': '1', '2': '7', '7': '2',
        '3': '8', '8': '3', '4': '9', '9': '4',
        # Caracteres especiais
        '@': '#', '#': '@', '!': '?', '?': '!', '$': '&', '&': '$',
        '%': '*', '*': '%'
    }
    return ''.join([substituicoes.get(c, c) for c in texto])

# Layout da Interface
layout = [
    [sg.Text("Digite o texto:", font=('Arial', 12))],
    [sg.Multiline(size=(50, 5), key='-INPUT-', font=('Arial', 12))],
    [sg.Button("Criptografar/Descriptografar"), sg.Button("Limpar")],
    [sg.Text("Resultado:", font=('Arial', 12))],
    [sg.Multiline(size=(50, 5), key='-OUTPUT-', font=('Arial', 12), disabled=True)],
    [sg.Button("Sair")]
]

# Configuração da Janela
window = sg.Window("Cifra Zenit Polar", layout, element_justification='center')

# Loop de Eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    elif event == "Criptografar/Descriptografar":
        texto = values['-INPUT-'].strip()
        if texto:
            window['-OUTPUT-'].update(zenit_polar(texto))
        else:
            sg.popup("Aviso", "Digite um texto primeiro!")
    elif event == "Limpar":
        window['-INPUT-'].update('')
        window['-OUTPUT-'].update('')

window.close()