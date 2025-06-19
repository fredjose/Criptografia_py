

import tkinter as tk
from tkinter import ttk, messagebox

def zenit_polar(texto):
    # Mapa de substituições (letras, números e caracteres especiais)
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

    resultado = []
    for caractere in texto:
        resultado.append(substituicoes.get(caractere, caractere))
    return ''.join(resultado)

def processar_texto():
    texto_original = entrada_texto.get("1.0", tk.END).strip()
    if not texto_original:
        messagebox.showwarning("Aviso", "Digite um texto para processar!")
        return

    texto_processado = zenit_polar(texto_original)
    saida_texto.delete("1.0", tk.END)
    saida_texto.insert(tk.END, texto_processado)

def limpar_campos():
    entrada_texto.delete("1.0", tk.END)
    saida_texto.delete("1.0", tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Cifra Zenit Polar")
root.geometry("500x400")
root.resizable(False, False)

# Estilo
fonte = ("Arial", 12)
cor_fundo = "#f0f0f0"
root.config(bg=cor_fundo)

# Widgets
tk.Label(root, text="Texto Original:", font=fonte, bg=cor_fundo).pack(pady=5)
entrada_texto = tk.Text(root, height=5, width=50, font=fonte, wrap=tk.WORD)
entrada_texto.pack(pady=5)

frame_botoes = tk.Frame(root, bg=cor_fundo)
frame_botoes.pack(pady=10)

btn_cripto = ttk.Button(frame_botoes, text="Criptografar/Descriptografar", command=processar_texto)
btn_cripto.pack(side=tk.LEFT, padx=5)

btn_limpar = ttk.Button(frame_botoes, text="Limpar", command=limpar_campos)
btn_limpar.pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Texto Processado:", font=fonte, bg=cor_fundo).pack(pady=5)
saida_texto = tk.Text(root, height=5, width=50, font=fonte, wrap=tk.WORD)
saida_texto.pack(pady=5)

# Rodar a aplicação
root.mainloop()