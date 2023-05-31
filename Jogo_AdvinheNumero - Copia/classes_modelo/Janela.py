import tkinter as tk
from tkinter import ttk
import NumeroGerado
import Jogada
from Jogada import Jogada as jogada
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
    num_id = Jogada.analisa_caracteres(TxtBarnumero)

    if num_id == 0:
        Jogada.compara_numeros(TxtBarnumero.get(), numero_gerado)
        gera_tabela(jogada.lista_jogadas)

    if num_id == 1:
        mensagens(num_id)
    elif num_id == 2:
        mensagens(num_id)


# Button
BtTestar = tk.Button(janela, text='Conferir números', command=test)
BtTestar.grid(column=1, row=4)

Btsair = tk.Button(janela, name='btsair', text="Sair", command=janela.destroy)
Btsair.grid(column=1, row=6, padx=4, pady=4)


# mostra determinada mensagem de acordo com o id de cada uma
def mensagens(msg_id):
    txt3 = TxtBarnumero.get()
    print(txt3, type(txt3))
    # Mensagens de erro
    if msg_id == 1:
        TxtBarnumero.insert(0, '')
        messagebox.showinfo(title=None, message='O número sugerido deve ter exatamente 4(quatro) caracteres')

    if msg_id == 2:
        messagebox.showinfo(title=None, message='O número sugerido nao pode conter caracteres repetidos')

    if msg_id == 3:
        messagebox.showinfo(title=None,
                            message=f"Pabens voce acertou o número!!\n Numero Sugerido:{txt3} \n Numeros Gerado: {numero_gerado}")
    if msg_id == 4:
        messagebox.showinfo(title=None, message=f'Vc errou o número')


ttk.Label(janela, text='-------------Jogadas-------------').grid(column=1, row=7, padx=10)
ttk.Label(janela, text='id  | numero sugerido | mesma posição |  outra posição').grid(column=1, row=11, padx=6)


def gera_tabela(lista_jogadas):
    # atributos do objeto :
    # id jogada, numsugerido,mesmap , outrap
    for i in range(len(lista_jogadas)):
        jog = lista_jogadas[i]
        tk.Label(janela, text=f' {jog.id_jogada}     |             {jog.numero_sugerido}           | '
                              f'           {jog.resultados}           ').grid(column=1, row=i + 12)


janela.mainloop()
