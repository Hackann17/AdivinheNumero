import tkinter as tk
from tkinter import ttk
import NumeroGerado
import Jogada
from tkinter import messagebox

id_jog = 0
# esse valor é gerado antes da tela aparecer e nao pode ser modificado no decorrer no codigo em hipotese alguma
numero_gerado = NumeroGerado.gerar_numero()

while numero_gerado == 'nada':
    numero_gerado = NumeroGerado.gerar_numero()

janela = tk.Tk()
janela.title('Adivinhe o número! Não repita cararteres e nao Passe de 4 digitos ')
# frm = ttk.Frame(janela, width=10, height=20)
# frm.grid( padx=10, pady=10)
# Label
Lbcabecalho = tk.Label(janela, text="Algarismos disponiveis:")
Lbcabecalho.grid(column=1, row=0)

Lbnumeros = tk.Label(janela, text='0123456789')
Lbnumeros.grid(column=1, row=1)

# Entrada de texto
TxtBarnumero = tk.Entry(janela)
TxtBarnumero.grid(column=1, row=2)


def test():
    print(numero_gerado)
    num_id = Jogada.analisa_caracteres(TxtBarnumero, numero_gerado)

    if num_id == 0:
        gera_tabela(lista_jogadas=Jogada.compara_numeros(str(TxtBarnumero.get), str(numero_gerado)))

    if num_id == 1:
        mensagens(num_id)
    elif num_id == 2:
        mensagens(num_id)


# Button
BtTestar = tk.Button(janela, text='Conferir números', command=test)
BtTestar.grid(column=1, row=4)

Btsair = tk.Button(janela, name='btsair', text="Sair", command=janela.destroy)
Btsair.grid(column=1, row=6, padx=5, pady=5)


# mostra determinada mensagem de acordo com o id de cada uma
def mensagens(id):
    # Mensagens de erro
    if id == 1:
        TxtBarnumero.insert(0, '')
        messagebox.showinfo(title=None, message='O número sugerido deve ter exatamente 4(quatro) caracteres')

    if id == 2:
        messagebox.showinfo(title=None, message='O número sugerido nao pode conter caracteres repetidos')

    if id == 3:
        txt = str(TxtBarnumero.get())
        messagebox.showinfo(title=None, message=f'Pabens voce acertou o número!!\n Numero Sugerido:{txt}'
                                                f'\n Numeros Gerado: {numero_gerado}')
    if id == 4:
        messagebox.showinfo(title=None, message=f'Vc errou o número')


def gera_tabela(lista_jogadas):
    print('opa')


janela.mainloop()

