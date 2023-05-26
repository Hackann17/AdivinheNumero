import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import NumeroGerado
import Jogada

# esse valor é gerado antes da tela aparecer e nao pode ser modificado no decorrer no codigo em hipotese alguma
numero_gerado = NumeroGerado.gerar_numero()

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


def test():
    Jogada.conta_caracteres(TxtBarnumero)


# Button
BtTestar = ttk.Button(frm, text='Conferir números', command=test())
BtTestar.grid(column=1, row=4)

Btsair = ttk.Button(frm, name='btsair', text="Sair", command=janela.destroy)
Btsair.grid(column=1, row=6, padx=5, pady=5)


# mostra determinada mensagem de acordo com o id de cada uma
def mensagens(id):
    # Mensagens de erro
    if id == 0:
        tk.messagebox.showinfo(title=None, message='O número sugerido deve ter exatamente 4(quatro) caracteres')

    if id == 1:
        tk.messagebox.showinfo(title=None, message='O número sugerido nao pode conter caracteres repetidos')


janela.mainloop()
