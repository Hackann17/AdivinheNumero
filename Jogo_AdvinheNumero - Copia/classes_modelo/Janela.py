import tkinter as tk
from tkinter import ttk
import Numero_Gerado
import Jogada

# esse valor é gerado antes da tela aparecer e nao pode ser modificado no decorrer no codigo em hipotese alguma
numero_gerado = Numero_Gerado.gerar_numero()

janela = tk.Tk()
janela.title('Adivinhe o número! Não repita cararteres e nao Passe de 4 digitos ')
frm = ttk.Frame(janela, width=100, height=200)
frm.grid(padx=10, pady=10)

# Label
Lbcabecalho = ttk.Label(frm, text="Algarismos disponiveis:")
Lbcabecalho.grid(column=1, row=0)

Lbnumeros = ttk.Label(frm, text='0123456789')
Lbnumeros.grid(column=1, row=1)

# Entrada de texto
TxtBarnumero = ttk.Entry(frm)
TxtBarnumero.grid(column=1, row=2)


def testar_num():
    Jogada.comparar_numero_sugerido(TxtBarnumero.get(), numero_gerado)


# Button
BtTestar = ttk.Button(frm, text='Conferir números', command=testar_num)
BtTestar.grid(column=1, row=4)

Btsair = ttk.Button(frm, name='btsair', text="Sair", command=janela.destroy)
Btsair.grid(column=1, row=6, padx=5, pady=5)

janela.mainloop()
